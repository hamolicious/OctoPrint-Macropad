from .base import MacroActionBase
import logging
import requests
from common_commands.send_gcode_commands import send_gcode_commands


class OffOnEnd(MacroActionBase):
	def __init__(self) -> None:
		super().__init__()

		self.url = '/api/settings'
		self.state = False

	def get_current_state(self) -> None:
		_, data = self.get_request()

		self.state = data.get('plugins').get('TpLinkAutoShutdown').get('smartPlug').get('auto')

		logging.info(f'Current State: {self.state}')

	def set_state(self, enabled: bool, silent=False) -> None:
		self.state = not enabled
		self.activate(silent, skip_state_check=True)

	def activate(self, silent=False, skip_state_check=False) -> None:
		if not skip_state_check:
			self.get_current_state()

		self.body = {
			"plugins": {
				"TpLinkAutoShutdown": {
					"smartPlug": {
						"auto": not self.state
					}
				}
			}
		}

		self.post_request()
		self.do_toggle()
		if not silent:
			self.send_lcd_command()

	def do_toggle(self) -> None:
		self.state = not self.state

	def send_lcd_command(self) -> None:
		send_gcode_commands('M300 1 260', f'M117 Shutdown on end:{self.state}')
