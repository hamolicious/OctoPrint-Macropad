from .base import MacroPadButtonBase
from gpiozero import Button
import logging
import requests


class PreHeatButton(MacroPadButtonBase):
	def __init__(self, gpio_number: int, name: str, api_key) -> None:
		super().__init__(gpio_number, name, api_key)

		self.url = 'http://192.168.0.75/api/printer/'
		self.body = {}
		self.headers = {
			'X-Api-Key': self.api_key,
			'Content-Type': 'application/json',
		}
		self.button = Button(gpio_number)

	def init(self) -> None:
		logging.info('Initiating')

	def set_state(self) -> None:
		self.body = {
		"target": 60,
		"command": "target"
		}
		with requests.post(self.url + 'bed', json=self.body, headers=self.headers) as r:
			pass

		self.body = {
			"targets": {
				"tool0": 200
			},
			"command": "target"
		}
		with requests.post(self.url + 'tool', json=self.body, headers=self.headers) as r:
			pass
