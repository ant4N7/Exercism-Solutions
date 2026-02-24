import re

def translate(text):
    pattern = r"\b(xr|y|[b-df-hj-npr-t-vwxz]*|[b-df-hj-npr-t-vwxz]*qu|q)([aeiouy]+)([\w']*)\b"

    result = []
    for m in re.finditer(pattern,text,flags = re.I):
        if m.group(1) == 'xr':
            result.append(m.group(0)+'ay')
        else:
            result.append(m.group(2)+m.group(3)+m.group(1)+'ay')
    return ' '.join(result)

