import actions


events = {
    'on_start': { 'target': actions.OffOnEnd().set_state, 'args': [ False, True ] },
    'on_connect': None,
    'on_error': None,
}



