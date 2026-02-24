from itertools import cycle,chain

def encode(message, rails):
    sequence = cycle(chain(range(rails-1),range(rails-1,0,-1)))
    chars = ['' for _ in range(rails)]
    for char in message:
        chars[next(sequence)] += char
    return ''.join(chars)


def decode(encoded_message, rails):
    sequence = cycle(chain(range(rails-1),range(rails-1,0,-1)))
    chars = list(encoded_message[::-1])
    blanks = [[] for _ in range(rails)]
    for _ in range(len(encoded_message)):
        n = next(sequence)
        for i,blank in enumerate(blanks):
            if i == n:
                blank.append('?')
            else:
                blank.append(None)
    for row in blanks:
        for i,blank in enumerate(row):
            if blank is not None:
                row[i] = chars.pop()
    # reset the sequence
    sequence = cycle(chain(range(rails-1),range(rails-1,0,-1)))
    decoded = []
    for _ in encoded_message:
        n = next(sequence)
        while blanks[n][0] is None:
            blanks[n].pop(0)
        decoded.append(blanks[n].pop(0))
    return ''.join(decoded)
