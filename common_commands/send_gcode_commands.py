import requests
import constants


def send_gcode_commands(*commands: list[str]) -> None:
	headers = {
		'X-Api-Key': constants.API_KEY,
		'Content-Type': 'application/json',
	}
	body = {
		"commands": commands,
		"parameters": {},
	}
	with requests.post(constants.PI_HOSTNAME + '/api/printer/command', json=body, headers=headers) as r:
		pass


