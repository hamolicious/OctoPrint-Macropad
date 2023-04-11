from .light_bar import LightBarButton
from .preheat import PreHeatButton
from .off import OffButton
from .resume import ResumeButton

with open('/home/pi/Documents/macro-pad/api.key', 'r') as f:
	api_key = f.read().splitlines()[0]

buttons = [
	LightBarButton(4, 'Lamp', api_key),
	PreHeatButton(17, 'Preheat', api_key),
	OffButton(27, 'Off', api_key),
	ResumeButton(22, 'Resume', api_key),
]

for b in buttons:
	b.init()

