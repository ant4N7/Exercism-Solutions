import re

def roman(n: int) -> str:
    #convert into roman without 9s, 5s, or 4s
    mcxd = 'M' * (n//1000%10) + 'C' * (n//100%10) + 'X' * (n//10%10) + 'I' * (n%10)

    #regex pattern to match 9s, 5s, and 4s
    pattern= r'''(^M*)(C{9})?(C{5})?(C{4})?(C*)        #match CM, D, or CD
                      (X{9})?(X{5})?(X{4})?(X*)        #match XC, L, or XL
                      (I{9})?(I{5})?(I{4})?(I*$)       #match IX, V, or IV'''

    #use finditer to access the groups
    for match in re.finditer(pattern,mcxd,flags=re.X):
        m,c9,c5,c4,c = match.group(1) ,match.group(2) ,match.group(3) ,match.group(4),match.group(5)
        x9,x5,x4,x   = match.group(6) ,match.group(7) ,match.group(8) ,match.group(9)
        i9,i5,i4,i   = match.group(10),match.group(11),match.group(12),match.group(13)

    #buld the return string
        return m+'CM'*(bool(c9))+'D'*(bool(c5))+'CD'*(bool(c4))+c \
                +'XC'*(bool(x9))+'L'*(bool(x5))+'XL'*(bool(x4))+x \
                +'IX'*(bool(i9))+'V'*(bool(i5))+'IV'*(bool(i4))+i
