from .base import MacroActionBase


class PreHeat(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/printer/'
		self.body = {}

		self.tool_temp = 200
		self.bed_temp = 60

	def activate(self) -> None:
		self.body = {
			"target": self.bed_temp,
			"command": "target"
		}
		self.post_request(url=self.url + 'bed')
		self.log(f'Heating bed to {self.bed_temp}C')

		self.body = {
			"targets": {
				"tool0": self.tool_temp
			},
			"command": "target"
		}
		self.post_request(url=self.url + 'tool')
		self.log(f'Heating extruder to {self.tool_temp}C')
