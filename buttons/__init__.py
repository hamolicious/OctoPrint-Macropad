from gpiozero import Button
import actions

buttons = {
	'resume_and_home': {
		'button': Button(22),
		'on_click': actions.Resume(),
		'on_hold': None,
	},
    'preheat_and_x': {
		'button': Button(17),
		'on_click': actions.PreHeat(),
		'on_hold': None,
	},
    'light_and_x': {
		'button': Button(4),
		'on_click': actions.LightBar(),
		'on_hold': None,
	},
    'off_on_end_and_x': {
		'button': Button(27),
		'on_click': actions.OffOnEnd(),
		'on_hold': None,
	},
}

