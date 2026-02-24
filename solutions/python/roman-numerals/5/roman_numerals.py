import re

def roman(n: int) -> str:
    
    #convert into roman without 9s, 5s, or 4s
    res = 'M' * (n//1000%10) + 'C' * (n//100%10) + 'X' * (n//10%10) + 'I' * (n%10)
    
    #re.sub each case
    res = re.sub(r'C{9}(?=X?I?)','CM',res)
    res = re.sub(r'C{5}(?=C?X?I?)','D',res)
    res = re.sub(r'C{4}(?=X?I?)','CD',res)
    
    res = re.sub(r'X{9}(?=I?)','XC',res)
    res = re.sub(r'X{5}(?=X?I?)','L',res)
    res = re.sub(r'X{4}(?=I?)','XL',res)
    
    res = re.sub(r'I{9}$','IX',res)
    res = re.sub(r'I{5}(?=I?)','V',res)
    res = re.sub(r'I{4}$','IV',res)

    return res
    