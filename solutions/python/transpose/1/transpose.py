from itertools import zip_longest

def transpose(text: str) -> str:
    
    if not text: return text
        
    strings = text.splitlines()
    if len(strings) == 1: return '\n'.join(text)
        
    add_spaces = max(len(s) for s in strings[1:])
    strings = [s.ljust(add_spaces) for s in strings[:-1]]+[strings[-1]]
    
    rows = []
    for column in zip_longest(*strings, fillvalue=''):
        rows.append(''.join(column))
    return '\n'.join(rows).rstrip()
