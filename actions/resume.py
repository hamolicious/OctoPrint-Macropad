from .base import MacroActionBase
import requests


class Resume(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/job'
		self.body = {
			"action": "resume",
			"command": "pause",
		}

	def activate(self) -> None:
		self.post_request()
		self.log('Resuming')

