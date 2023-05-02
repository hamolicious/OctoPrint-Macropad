from .base import MacroActionBase


class MotorsOff(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/command'
		self.body = {
			'commands': [
				'M18'
			],
			'parameters': {}
		}

	def activate(self) -> None:
		self.post_request()
		self.log('Disabling Motors')
