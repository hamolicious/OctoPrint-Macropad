from .base import MacroActionBase
import requests


class Home(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/printhead'
		self.body = {}

	def activate(self) -> None:
		self.body = {
			'command': 'home',
			'axes': [ 'x', 'y', 'z' ],
		}
		self.post_request()
		self.log('Homing')
