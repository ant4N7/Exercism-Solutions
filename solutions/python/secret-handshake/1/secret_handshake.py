ACTIONS = ['jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str):
    if binary_str[0] == '1':
        return [action for i, action in enumerate(ACTIONS) if binary_str[i+1] == '1']
    return [action for i, action in enumerate(ACTIONS) if binary_str[i+1] == '1'][::-1]
