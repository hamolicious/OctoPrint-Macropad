

with open('/home/pi/Documents/macro-pad/api.key', 'r') as f:
	API_KEY = f.read().splitlines()[0]

HELD_FOR_COUNTS_AS_HOLD = 0.5
PI_HOSTNAME = 'http://192.168.0.75'

