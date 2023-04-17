from .base import MacroActionBase
import logging
import requests


class Home(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = self.pi_host + '/api/printer/printhead'
		self.body = {}

	def activate(self) -> None:
		self.body = {
			'command': 'home',
			'axes': [ 'x', 'y', 'z' ],
		}
		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			print(r.content)
