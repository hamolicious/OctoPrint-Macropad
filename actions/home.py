from .base import MacroActionBase


class Home(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/printhead'
		self.body = {
			'command': 'home',
			'axes': [ 'x', 'y', 'z' ],
		}

	def activate(self) -> None:
		self.post_request()
		self.log('Homing')
