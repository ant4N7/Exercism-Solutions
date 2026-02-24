import re
PATTERN = re.compile(r' '.join([r'([AKQJ0-9]{1,2})([HCDS]{1})']*5))
CARD_VALUES = [None,'2','3','4','5','6','7','8','9','10','J','Q','K','A']

def best_hands(hands: list[str]) -> list[str]:
    """return the best hand or hands from a list of hands"""
    hands_data = [score(hand) for hand in hands]
    return [hand for hand in hands if score(hand) == max(hands_data)]

def sort_by_frequency(hand: list[str]) -> list[int]:
    """return the card values sorted by descending frequency then descending value"""
    m = PATTERN.match(hand)
    values = [CARD_VALUES.index(m[i]) for i in range(1,10,2)]
    frequency = {item: values.count(item) for item in set(values)}
    return sorted(values, key=lambda x: (-frequency[x], -x))

def score(hand: list[str]) -> tuple[int,list[int]]:
    """prepend the sorted values with a rank based on the values"""
    m = PATTERN.match(hand)
    values = sort_by_frequency(hand)
    if values == [13,4,3,2,1]: values = [4,3,2,1,0]
        
    flush = m[2]==m[4]==m[6]==m[8]==m[10]
    straight = all(values[i]-1==values[i+1] for i in range(4))
    quads = values[0]==values[1]==values[2]==values[3]
    boat = values[0]==values[1]==values[2] and values[3]==values[4]
    trips = values[0]==values[1]==values[2]
    two_pair = values[0]==values[1] and values[2]==values[3]
    pair = values[0]==values[1]
    
    if straight and flush: return (8,values)
    if quads: return (7,values)
    if boat: return (6,values)
    if flush: return (5,values)
    if straight: return (4,values)
    if trips: return (3,values)
    if two_pair: return (2,values)
    if pair: return (1,values)
    return (0,values)
    