import re
PATTERN = r' '.join([r'([AKQJ0-9]{1,2})([HCDS]{1})']*5)
CARD_VALUES = [None,'2','3','4','5','6','7','8','9','10','J','Q','K','A']

def best_hands(hands):
    stop_cond,counter = len(hands)-1,0
    while len(hands)>1:
        h2,h1 = hands.pop(),hands.pop()
        if score(h1)>score(h2): hands.append(h1)
        elif score(h1)<score(h2): hands.append(h2)
        else: hands = [h1,h2] + hands
        counter+=1
        if counter == stop_cond: break
    return hands
    

def score(hand):
    m = re.match(PATTERN,hand)
    values = sorted(CARD_VALUES.index(m[i]) for i in range(1,10,2))
    if values == [1,2,3,4,13]: values = [0,1,2,3,4]
    
    ranks = 0x200000 * (all(values[i]+1==values[i+1] for i in range(4)) and  m[2]==m[4]==m[6]==m[8]==m[10])*sum(values) +\
            0x100000 * (values[0]==values[3] or values[1]==values[4])*values[2] +\
            0x80000 * (len(set(values))==2 and values.count(values[2])==3)*values[2] +\
            0x40000 * (m[2]==m[4]==m[6]==m[8]==m[10]) +\
            0x20000 * (all(values[i]+1==values[i+1] for i in range(4))) +\
            0x10000 * (values.count(values[2]) == 3) +\
            0x8000 * (values.count(values[1])==2 and values.count(values[3])==2) +\
            0x4000 * (sum(values.count(values[i])==2 for i in range(5)) == 2)
    
    cards = sum(2**n for n in values)
    return ranks+cards
