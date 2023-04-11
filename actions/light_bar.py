from .base import MacroActionBase
import logging
import requests


class LightBar(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = 'http://192.168.0.75/api/plugin/gpiocontrol'
		self.toggle = ['turnGpioOn', 'turnGpioOff']
		self.body = {
			'id': 0,
			'command': 'turnGpioOn',
		}

	def init(self) -> None:
		logging.info('Initiating')
		self.get_current_state()

	def get_current_state(self) -> None:
		with requests.get(self.url, json=self.body, headers=self.headers) as r:
			data = r.text[2:2:]

		if data == 'on'  and self.toggle[0] != 'turnGpioOn'  : self.do_toggle()
		if data == 'off' and self.toggle[0] != 'turnGpioOff' : self.do_toggle()

		logging.info(f'Current State: {data}')

	def activate(self) -> None:
		state = 'ON' if self.body.get('command') == 'turnGpioOn' else 'OFF'
		logging.info(f'Setting State: {state}')

		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			pass
		self.do_toggle()

	def do_toggle(self) -> None:
		item = self.toggle.pop(0)
		self.toggle.append(item)
		self.body['command'] = self.toggle[0]

