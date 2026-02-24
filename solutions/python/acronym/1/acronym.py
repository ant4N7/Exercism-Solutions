def abbreviate(words: str) -> str:
    return ''.join(s[0].upper() for s in words.replace('-',' ').replace('_','').split())
