def is_paired(input_string):
    raw_string = ''
    for char in input_string:
        if char in '({[':
            raw_string += char
        if char in ')}]':
            raw_string += char+','

    try: 
        if not raw_string:
            raise ValueError
        eval(raw_string)
    except ValueError: return True
    except SyntaxError: return False
    except Exception: return True
    else: return True
