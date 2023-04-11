import requests
from constants import API_KEY


def send_gcode_commands(*commands: list[str]) -> None:
	headers = {
		'X-Api-Key': API_KEY,
		'Content-Type': 'application/json',
	}
	body = {
		"commands": commands,
		"parameters": {},
	}
	with requests.post('http://192.168.0.75/api/printer/command', json=body, headers=headers) as r:
		pass


