from .base import MacroActionBase
import common_commands
import logging
import requests


class Purge(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/tool'
		self.body = {}

	def activate(self) -> None:
		self.body ={
			"amount": 50,
			"command": "extrude"
		}
		self.post_request()
