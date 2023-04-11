from .base import MacroActionBase
import common_commands
import logging
import requests


class Off(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = 'http://192.168.0.75/api/plugin/TpLinkAutoShutdown'
		self.body = {}

	def activate(self) -> None:
		self.body = {
			"value": "False",
			"command": "turnOff"
		}
		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			print(r.content)
