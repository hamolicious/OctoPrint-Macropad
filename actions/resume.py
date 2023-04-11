from .base import MacroActionBase
import logging
import requests


class Resume(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = 'http://192.168.0.75/api/job'
		self.body = {
			"action": "resume",
			"command": "pause",
		}

	def activate(self) -> None:
		with requests.post(self.url, json=self.body, headers=self.headers) as r:
			pass

