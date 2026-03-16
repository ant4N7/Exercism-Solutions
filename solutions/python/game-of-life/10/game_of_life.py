"""Game of Life"""
NEIGHBOR_OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """One tick of Conway's Game of Life does not modify input."""
    
    # Early return for edge case
    if not matrix: 
        return matrix

    # initialize result matrix
    result = []

    # precompute height and width for bounds checking
    height, width = len(matrix), len(matrix[0])

    # This is a bit confusing but...
    # I'm using binary and boolean logic and bit shifting to find the index of this table,
    # and then using these anonymous functions to fetch the view we need from the matrix.
    view_table = [
        lambda r,c: matrix[r-1][c-1:c+2] + [matrix[r][c-1]] + [matrix[r][c+1]] + matrix[r+1][c-1:c+2],
        lambda r,c: matrix[r-1][c-1:c+2] + [matrix[r][c-1]] + [matrix[r][c+1]],
        lambda r,c: matrix[r-1][c-1:c+1] + [matrix[r][c-1]] + matrix[r+1][c-1:c+1],
        lambda r,c: [matrix[r][c-1]] + matrix[r-1][c-1:c+1],
        lambda r,c: matrix[r-1][c:c+2] + [matrix[r][c+1]] + matrix[r+1][c:c+2],
        lambda r,c: [matrix[r][c+1]] + matrix[r-1][c:c+2],
        None,
        None,
        lambda r,c: [matrix[r][c-1]] + [matrix[r][c+1]] + matrix[r+1][c-1:c+2],
        None,
        lambda r,c: [matrix[r][c-1]] + matrix[r+1][c-1:c+1],
        None,
        lambda r,c: [matrix[r][c+1]] + matrix[r+1][c:c+2],
    ]

    # Main Loop
    for row, row_values in enumerate(matrix):
        new_row = []
        for col, cell_value in enumerate(row_values):
            is_top, is_left, is_bottom, is_right = row == 0, col == 0, row == height-1, col == width-1
            view_table_index = is_top << 3 ^ is_left << 2 ^ is_right << 1 ^ is_bottom
            live_neighbors = sum(view_table[view_table_index](row,col))
            if live_neighbors == 3 or cell_value and live_neighbors == 2:
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result