def convert(number):
    result = ''
    result += 'Pling' if not number % 3 else ''
    result += 'Plang' if not number % 5 else ''
    result += 'Plong' if not number % 7 else ''
    result += str(number) if number % 3 and number % 5 and number % 7 else ''
    return result
