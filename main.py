import logging
logging.basicConfig(level=logging.INFO)
logging.info('Loading')

import requests
import common_commands
import constants
from time import sleep, time
from buttons import buttons


# Wait for OctoPrint to start
headers = {
	'X-Api-Key': constants.API_KEY,
	'Content-Type': 'application/json',
}
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

# Begin
logging.info('Starting')
while True:
	try:
		for b in buttons.values():
			if b.get('button').is_pressed:
				if b.get('pressed_at') == None:
					b['pressed_at'] = time()
			elif (not b.get('button').is_pressed) and (b.get('pressed_at') is not None):
				held_for = abs(time() - b.get('pressed_at'))
				b['pressed_at'] = None

				if held_for > constants.HELD_FOR_COUNTS_AS_HOLD:
					if b.get('on_hold') is not None:
						common_commands.send_gcode_commands('M300 P50')
						print('activating "on_hold"')
						b.get('on_hold').activate()
				else:
					if b.get('on_click') is not None:
						common_commands.send_gcode_commands('M300 P50')
						print('activating "on_click"')
						b.get('on_click').activate()

	except Exception as e:
		logging.error(f'ERR: {e}')
		continue

	button_press_sum = sum([int(b.get('button').is_pressed) for b in buttons.values()])
	if button_press_sum == 0:
		button_lock = False


