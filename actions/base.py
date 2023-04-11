import logging
import constants


class MacroActionBase:
	def __init__(self) -> None:
		self.url = ''
		self.body = {}
		self.api_key: str = constants.API_KEY
		self.headers = {
			'X-Api-Key': self.api_key,
			'Content-Type': 'application/json',
		}

	def init(self) -> None:
		...

	def get_current_state(self) -> None:
		...

	def activate(self) -> None:
		...

