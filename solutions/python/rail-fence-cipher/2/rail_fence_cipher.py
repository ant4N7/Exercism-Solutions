from itertools import cycle,chain

def encode(message, rails):
    sequence = cycle(chain(range(rails-1),range(rails-1,0,-1)))
    chars = ['' for _ in range(rails)]
    for char in message:
        chars[next(sequence)] += char
    return ''.join(chars)

def decode(encoded_message, rails):
    sequence = cycle(chain(range(rails-1,0,-1),range(rails-1)))
    chars = list(encoded_message)
    rail_lens = [0 for _ in range(rails)]
    for _ in encoded_message:
        rail_lens[next(sequence)] += 1
    
    fence = [[] for _ in range(rails)]
    for i,blank in enumerate(fence):
        for _ in range(rail_lens[i]):
            blank += chars.pop()

    # reset the sequence
    sequence = cycle(chain(range(rails-1,0,-1),range(rails-1)))
    decoded = []
    for _ in encoded_message:
        n = next(sequence)
        decoded.append(fence[n].pop())
    return ''.join(decoded)
