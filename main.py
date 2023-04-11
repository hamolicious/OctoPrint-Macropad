import logging
logging.basicConfig(level=logging.INFO)
logging.info('Loading')

import requests
import common_commands
import constants

# Wait for OctoPrint to start
headers = {
	'X-Api-Key': constants.API_KEY,
	'Content-Type': 'application/json',
}
from time import sleep
while True:
	try:
		with requests.get('http://192.168.0.75/api/server', headers=headers) as r:
			data = r.content
			if r.status_code == 200:
				break
			logging.info(f'OctoPrint is not ready yet: {data}')
	except Exception as e:
		logging.info(f'OctoPrint is not ready yet: {e}')
		sleep(1)

# Notify that MacroPad is ready
common_commands.send_gcode_commands(f'M117 MacroPad Ready', 'M300 P100 S100')

# Setup
from buttons import buttons
button_lock = False

# Begin
logging.info('Starting')
while True:
	try:
		for b in buttons:
			if b.is_pressed() and button_lock is False:
				common_commands.send_gcode_commands('M300 P50')
				b.set_state()
				button_lock = True
	except Exception as e:
		logging.error(f'ERR: {e}')
		continue

	button_press_sum = sum([int(b.is_pressed()) for b in buttons])
	if button_press_sum == 0:
		button_lock = False


