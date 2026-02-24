from collections import deque


def can_chain(dominoes):
    # early return conditions
    if not dominoes:
        return dominoes
    if len(dominoes) == 1 and dominoes[0][0] == dominoes[0][1]:
        return dominoes

    d = deque(dominoes,len(dominoes))
    result = deque([d.popleft()],len(dominoes))
    loop_counter, rotate_counter = 0, 0
    while d:
        loop_counter += 1

        # see if the domino can attach to the chain
        a,b = d.popleft()
        if result[-1][1] == a:
            result.append((a,b))
        elif result[-1][1] == b:
            result.append((b,a))
        else: # put it back on the deque
            d.append((a,b))

        # see if we've used all the dominoes to make a chain
        if len(result) == result.maxlen and result[0][0] == result[-1][1]:
            return result

        # try backtracking if possible
        if not loop_counter % len(d) and result[0][0] == result[-1][1]:
            result.rotate(1)
            rotate_counter+=1

        # give up
        if rotate_counter == d.maxlen or loop_counter > d.maxlen*2:
            break
