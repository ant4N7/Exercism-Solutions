def is_isogram(string):
    just_letters = ''.join(sorted(string.lower())).lstrip(' -') # remove non-letters
    return len(just_letters) == len(set(just_letters)) #remove duplicate letters and compare length
