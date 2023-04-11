import logging


class MacroPadButtonBase:
	def __init__(self, gpio_number: int, name: str, api_key: str) -> None:
		self.gpio_number: int = gpio_number
		self.name: str = name
		self.url = ''
		self.body = {}
		self.button = None
		self.api_key: str = api_key

	def init(self) -> None:
		...

	def get_current_state(self) -> None:
		...

	def set_state(self) -> None:
		...

	def is_pressed(self) -> bool:
		if self.button is None:
			return False
		return self.button.is_pressed





