from .base import MacroActionBase


class LightBar(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/plugin/gpiocontrol'
		self.body = {
			'id': 0,
			'command': 'turnGpioOn',
		}

		self.ON_STATE = 'turnGpioOn'
		self.OFF_STATE = 'turnGpioOff'
		self.current_state = None

	def get_current_state(self) -> None:
		_, data = self.get_request()
		self.current_state = self.ON_STATE if data[0] == 'on' else self.OFF_STATE
		self.log(f'Current State: {self.current_state.replace("turnGpio", "")}')

	def activate(self) -> None:
		self.get_current_state()

		if self.current_state == self.ON_STATE:
			self.current_state = self.OFF_STATE
		else:
			self.current_state = self.ON_STATE

		self.log(f'Setting State: {self.current_state.replace("turnGpio", "")}')

		self.body['command'] = self.current_state
		_, data = self.post_request()

