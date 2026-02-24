from itertools import cycle

def spiral_matrix(size: int) -> list[list[int]]:
    """generate a matrix in a spiral pattern"""
    # early return for 0 size
    if size == 0: return []

    # local constant iterator
    direction = cycle([(0,1),(1,0),(0,-1),(-1,0)])
    
    # initialize the output and set the first value
    output = [[0 for _ in range(size)] for _ in range(size)]
    output[0][0] = 1

    # main logic
    r,c = 0,0
    nr,nc = next(direction)
    for n in range(2,size*size+1):
        r,c = r+nr,c+nc
        if 0<=r<size and 0<=c<size and output[r][c] == 0:
            output[r][c] = n
        else:
            r,c = r-nr,c-nc
            nr,nc = next(direction)
            r,c = r+nr,c+nc
            output[r][c] = n
    return output
