from .base import MacroActionBase
import logging
import requests


class PreHeat(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/'
		self.body = {}

	def activate(self) -> None:
		self.body = {
			"target": 60,
			"command": "target"
		}
		self.post_request(url=self.url + 'bed')

		self.body = {
			"targets": {
				"tool0": 200
			},
			"command": "target"
		}
		self.post_request(url=self.url + 'tool')
