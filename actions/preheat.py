from .base import MacroActionBase
import logging
import requests


class PreHeat(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = 'http://192.168.0.75/api/printer/'
		self.body = {}

	def activate(self) -> None:
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
