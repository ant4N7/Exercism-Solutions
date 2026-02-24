import re

def score(word):
    pattern = r'([aeioulnrst])?([dg])?([bcmp])?([fhvwy])?(k)?([jx])?([qz])?'
    score = 0
    for match in re.finditer(pattern,word,flags=re.I):
        if match[1]: score += 1
        if match[2]: score += 2
        if match[3]: score += 3
        if match[4]: score += 4
        if match[5]: score += 5
        if match[6]: score += 8
        if match[7]: score += 10
    return score
