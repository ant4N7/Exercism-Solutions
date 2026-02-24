from itertools import cycle,chain

def fence_pattern(rails: int, message_length: int) -> list[tuple[int,int]]:
    """returns a list of tuples mapping the rail to the index of the character in the message"""
    sequence = cycle(chain(range(rails-1),range(rails-1,0,-1)))
    return sorted((s,i) for s,i in zip(sequence,range(message_length)))

def encode(message: str, rails: int) -> str:
    return ''.join(message[i] for _,i in fence_pattern(rails,len(message)))

def decode(encoded_message: str, rails: int) -> str:
    """changes the sort key of the fence pattern to put the message back in the original order"""
    char_map = zip(fence_pattern(rails,len(encoded_message)),encoded_message)
    return ''.join(ch for _,ch in sorted(char_map, key = lambda i: i[0][1]))
