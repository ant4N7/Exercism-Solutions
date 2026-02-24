import re

def count_words(s: str) -> dict[str, int]:
    return {w:[m[0] for m in re.finditer(r'[a-z0-9]+(\'\w\w?)?',s.casefold())].count(w)\
            for w in [m[0] for m in re.finditer(r'[a-z0-9]+(\'\w\w?)?',s.casefold())]}
