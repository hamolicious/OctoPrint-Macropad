from .base import MacroPadButtonBase
from gpiozero import Button
import logging
import requests
from common_commands.send_gcode_commands import send_gcode_commands


class OffButton(MacroPadButtonBase):
	def __init__(self, gpio_number: int, name: str, api_key) -> None:
		super().__init__(gpio_number, name, api_key)

		self.url = 'http://192.168.0.75/api/settings'
		self.state = False
		self.headers = {
			'X-Api-Key': self.api_key,
			'Content-Type': 'application/json',
		}
		self.button = Button(gpio_number)

	def init(self) -> None:
		logging.info('Initiating')
		self.get_current_state()

	def get_current_state(self) -> None:
		with requests.get(self.url, json=self.body, headers=self.headers) as r:
			data = r.json()

		self.state = data.get('plugins').get('TpLinkAutoShutdown').get('smartPlug').get('auto')

		logging.info(f'Current State: {self.state}')

	def set_state(self) -> None:
		state = not self.state
		logging.info(f'Setting State: {state}')

		self.body = {
			"plugins": {
				"TpLinkAutoShutdown": {
					"smartPlug": {
						"auto": not self.state
					}
				}
			}
		}

		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			pass
		self.do_toggle()
		self.send_lcd_command()

	def do_toggle(self) -> None:
		self.state = not self.state

	def send_lcd_command(self) -> None:
		send_gcode_commands('M300 1 260', f'M117 Shutdown on end:{self.state}')
