from .base import MacroActionBase
import logging
import requests
from common_commands.send_gcode_commands import send_gcode_commands


class OffOnEnd(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = self.pi_host + '/api/settings'
		self.state = False

	def init(self) -> None:
		logging.info('Initiating')
		self.get_current_state()

	def get_current_state(self) -> None:
		with requests.get(self.url, json=self.body, headers=self.headers) as r:
			data = r.json()

		self.state = data.get('plugins').get('TpLinkAutoShutdown').get('smartPlug').get('auto')

		logging.info(f'Current State: {self.state}')

	def set_state(self, enabled: bool, silent=False) -> None:
		self.state = True
		self.activate(silent)

	def activate(self, silent=False) -> None:
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
		if not silent:
			self.send_lcd_command()

	def do_toggle(self) -> None:
		self.state = not self.state

	def send_lcd_command(self) -> None:
		send_gcode_commands('M300 1 260', f'M117 Shutdown on end:{self.state}')
