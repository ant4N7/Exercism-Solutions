import re

def roman(n: int) -> str:
    just10s = 'M' * (n//1000%10) + 'C' * (n//100%10) + 'X' * (n//10%10) + 'I' * (n%10)
    pattern= r'''(^M*)(C{9})?(C{5})?(C{4})?(C*)        #match CM, D, or CD
                      (X{9})?(X{5})?(X{4})?(X*)        #match XC, L, or XL
                      (I{9})?(I{5})?(I{4})?(I*$)'''    #match IX, V, or IV
    for match in re.finditer(pattern,just10s,flags=re.X):
        m,c9,c5,c4,c = match.group(1),match.group(2),match.group(3),match.group(4),match.group(5)
        x9,x5,x4,x = match.group(6),match.group(7),match.group(8),match.group(9)
        i9,i5,i4,i = match.group(10),match.group(11),match.group(12),match.group(13)
        return m+'CM'*(not not c9)+'D'*(not not c5)+'CD'*(not not c4)+c \
               +'XC'*(not not x9)+'L'*(not not x5)+'XL'*(not not x4)+x \
               +'IX'*(not not i9)+'V'*(not not i5)+'IV'*(not not i4)+i

