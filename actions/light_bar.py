from .base import MacroActionBase
import logging
import requests


class LightBar(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = self.pi_host + '/api/plugin/gpiocontrol'
		self.ON_STATE = 'turnGpioOn'
		self.OFF_STATE = 'turnGpioOff'
		self.current_state = None
		self.body = {
			'id': 0,
			'command': 'turnGpioOn',
		}

	def init(self) -> None:
		logging.info('Initiating')
		self.get_current_state()

	def get_current_state(self) -> None:
		with requests.get(self.url, json=self.body, headers=self.headers) as r:
			data = r.json()[0].lower()

		self.current_state = self.ON_STATE if data == 'on' else self.OFF_STATE

	def activate(self) -> None:
		self.get_current_state()

		if self.current_state == self.ON_STATE:
			self.current_state = self.OFF_STATE
		else:
			self.current_state = self.ON_STATE

		self.body['command'] = self.current_state

		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			pass
		self.do_toggle()

	def do_toggle(self) -> None:
		item = self.toggle.pop(0)
		self.toggle.append(item)
		self.body['command'] = self.toggle[0]

