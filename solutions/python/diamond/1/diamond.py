from string import ascii_uppercase as caps

def rows(letter: str) -> list:
    #formula:   ws*n + caps[i]*b + ws*m + caps[i] + ws*n
    #start in the middle, build the bottom, then put the top on
    
    bottom = []
    for n in range(caps.index(letter)+1):
        i = caps.index(letter)-n
        b = bool(i)
        m = 2*i-1
        row = ' '*n + caps[i]*b + ' '*m + caps[i] + ' '*n
        bottom.append(row)
        
    top = bottom[:0:-1]
    return top + bottom
