def convert(number):
    result = ''
    result += 'Pling' if not number % 3 else ''
    result += 'Plang' if not number % 5 else ''
    result += 'Plong' if not number % 7 else ''
    result += str(number) if not result else ''
    return result
