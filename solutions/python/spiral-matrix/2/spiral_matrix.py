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
    row, column = 0,0
    next_row, next_column = next(direction)
    
    for n in range(2,size*size+1):
        row, column = row+next_row, column+next_column
        if 0<=row<size and 0<=column<size and output[row][column] == 0:
            output[row][column] = n
            
        else:  # step back, change direction, and continue
            row, column = row-next_row, column-next_column
            next_row, next_column = next(direction)
            row, column = row+next_row, column+next_column
            output[row][column] = n
            
    return output
