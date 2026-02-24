import re

def roman(n: int) -> str:
    just10s = 'M' * (n//1000%10) + 'C' * (n//100%10) + 'X' * (n//10%10) + 'I' * (n%10)
    pattern= r'(^M*)(C{9})?(C{5})?(C{4})?(C*)(X{9})?(X{5})?(X{4})?(X*)(I{9})?(I{5})?(I{4})?(I*$)'
    for match in re.finditer(pattern,just10s):
        a,b,c,d,e,f,g,h,i,j,k,l,m = match.group(1),match.group(2),match.group(3),match.group(4),match.group(5),match.group(6),match.group(7),match.group(8),match.group(9),match.group(10),match.group(11),match.group(12),match.group(13)
        return a+'CM'*(not not b)+'D'*(not not c)+'CD'*(not not d)+e+'XC'*(not not f)+'L'*(not not g)+'XL'*(not not h)+i+'IX'*(not not j)+'V'*(not not k)+'IV'*(not not l)+m

