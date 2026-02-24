import re

def score(word):
    word = re.sub(r'[aeioulnrst]','+1' ,word.lower())
    word = re.sub(r'[dg]'        ,'+2' ,word)
    word = re.sub(r'[bcmp]'      ,'+3' ,word)
    word = re.sub(r'[fhvwy]'     ,'+4' ,word)
    word = re.sub(r'k'           ,'+5' ,word)
    word = re.sub(r'[jx]'        ,'+8' ,word)
    word = re.sub(r'[qz]'        ,'+10',word)
    return eval('0'+word)
