def line_up(name, number):
    return f'{name}, you are the {number}{resolve_suffix(number)} customer we serve today. Thank you!'

def resolve_suffix(number):
    last_two_digits = number % 100
    last_digit = number % 10
    if last_two_digits in {11,12,13} or last_digit not in {0,1,2,3}:
        return 'th'
    return_string = ['th', 'st', 'nd', 'rd']
    return return_string[last_digit]