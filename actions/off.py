from .base import MacroActionBase
import common_commands
import logging
import requests


class Off(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/plugin/TpLinkAutoShutdown'
		self.body = {}

	def activate(self) -> None:
		self.body = {
			"value": "False",
			"command": "turnOff"
		}
		self.post_request()
