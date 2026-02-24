import re

def translate(text: str) -> str:
    consonants = r"[b-df-hj-npr-t-vwxz]"    #matches consonants except for q
    vowels = r"[aeiouy]"                    #matches vowels and y
    pattern = r"\b(xr|y|%s*|%s*qu|q)(%s+)([\w']*)\b" % (consonants,consonants,vowels)

    result = []
    for m in re.finditer(pattern,text,flags = re.I):
        vowel_group = m.group(2)
        remaining = m.group(3)
        prefix = m.group(1)
        if prefix == 'xr':
            result.append(m.group(0)+'ay')
        else:
            result.append(vowel_group+remaining+prefix+'ay')
    return ' '.join(result)

