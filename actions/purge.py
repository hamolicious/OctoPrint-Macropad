from .base import MacroActionBase
import common_commands
import requests


class Purge(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/tool'
		self.body = {}
		self.purge_amount = 50

	def activate(self) -> None:
		self.body ={
			"amount": self.purge_amount,
			"command": "extrude"
		}
		self.post_request()
		self.log(f'Purging {self.purge_amount}mm')
