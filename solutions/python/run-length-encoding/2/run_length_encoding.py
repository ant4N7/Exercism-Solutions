def decode(string):
    multiplier = ''
    result = ''
    for char in string:
        if char.isdigit():
            multiplier += char
        else:
            result += char*int(multiplier) if multiplier else char
            multiplier = ''
    return result


def encode(string):
    counter = 1
    result = ''
    for i,char in enumerate(string):
        if i == len(string)-1:
            result += str(counter) + string[-1] if counter > 1 else char
        elif char == string[i+1]:
            counter += 1
        else:
            result += str(counter) + char if counter > 1 else char
            counter = 1
    return result
