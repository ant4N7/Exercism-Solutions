def decode(string):
    multiplier = ''
    result = ''
    for char in string:
        if char.isdigit():
            multiplier += char
        else:
            if multiplier:
                result += char*int(multiplier)
            else:
                result += char
            multiplier = ''
    return result


def encode(string):
    counter = 1
    result = ''
    for i,char in enumerate(string):
        if i == len(string)-1:
            if counter == 1:
                result += char
            else:
                result += str(counter) + string[-1]
        elif char == string[i+1]:
            counter += 1
        else:
            if counter == 1:
                result += char
            else:
                result += str(counter) + char
            counter = 1
    return result
