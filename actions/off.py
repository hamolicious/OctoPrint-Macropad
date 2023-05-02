from .base import MacroActionBase


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
		self.log('Shutting down printer')
