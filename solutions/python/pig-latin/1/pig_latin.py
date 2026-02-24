def translate(text: str) -> str:
    words = text.split(' ')
    vowels = tuple('aeiou')
    rule1 = vowels + ('yt','xr')
    rule4 = tuple('bcdfghjklmnpqrstvwx')
    rule2_3 = rule4 + ('y',)
    result = ''
    for word in words:
        if word.startswith(rule1):
            result += word + 'ay '
            continue
        elif word.startswith(rule4) and word.lstrip(str(rule4))[0] == 'y':
            result += word.lstrip(str(rule4))+word[:word.index('y')]+'ay '
            continue
        elif word.startswith(rule2_3) and 'qu' in word:
            result += word.lstrip(str(rule2_3 + ('qu',)))+word.rstrip(word.lstrip(str(rule2_3 + ('qu',))))+'ay '
            continue
        else:
            result += word.lstrip(str(rule2_3))+word.rstrip(word.lstrip(str(rule2_3)))+'ay '
    return result.rstrip(' ')
