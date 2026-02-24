from itertools import cycle

def spiral_matrix(size: int) -> list[list[int]]:
    """generate a matrix in a spiral pattern"""
    
    # early return for 0 size
    if size == 0: return []

    # local constant iterator
    deltas = cycle([(0,1),(1,0),(0,-1),(-1,0)])
    
    # initialize the output and set the first value
    output = [[None]*size for _ in range(size)]
    output[0][0] = 1

    # main logic
    r, c = 0,0
    dr, dc = next(deltas)
    
    for n in range(2,size*size+1):
        # go to the next cell
        r, c = r+dr, c+dc

        # make sure we're within the bounds and haven't already updated
        if 0<=r<size and 0<=c<size and output[r][c] is None:
            output[r][c] = n
            
        else:  # step back, change direction, and continue
            r, c = r-dr, c-dc
            dr, dc = next(deltas)
            r, c = r+dr, c+dc
            output[r][c] = n
            
    return output
