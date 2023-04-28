import logging
import requests
import constants
from urllib import parse


class MacroActionBase:
	def __init__(self) -> None:
		self.url = ''
		self.body = {}
		self.api_key: str = constants.API_KEY
		self.headers = {
			'X-Api-Key': self.api_key,
			'Content-Type': 'application/json',
		}
		self.pi_host = constants.PI_HOSTNAME

	def get_current_state(self) -> None:
		...

	def activate(self) -> None:
		...

	def post_request(self, body:dict=None, headers:dict=None, url:str=None) -> tuple:
		full_url = parse.urljoin(self.pi_host, (url if url is not None else self.url))
		if headers is None : headers = self.headers
		if body is None : body = self.body

		with requests.post(full_url, json=body, headers=headers) as r:
			return (r.status_code, r.json())

	def get_request(self, body:dict=None, headers:dict=None, url:str=None) -> tuple:
		full_url = parse.urljoin(self.pi_host, (url if url is not None else self.url))
		if headers is None : headers = self.headers
		if body is None : body = self.body

		with requests.get(full_url, json=body, headers=headers) as r:
			return (r.status_code, r.json())
