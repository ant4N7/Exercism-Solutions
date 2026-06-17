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


    def get_neighbor_view(r,c):
        is_top, is_left, is_bottom, is_right = r == 0, c == 0, r == height-1, c == width-1
        if not is_top and not is_left and not is_bottom and not is_right:
            return matrix[r-1][c-1:c+2] + [matrix[r][c-1]] + [matrix[r][c+1]] + matrix[r+1][c-1:c+2]
        if is_top and is_left:
            return [matrix[r][c+1]] + matrix[r+1][c:c+2]
        if is_top and is_right:
            return [matrix[r][c-1]] + matrix[r+1][c-1:c+1]
        if is_bottom and is_left:
            return [matrix[r][c+1]] + matrix[r-1][c:c+2]
        if is_bottom and is_right:
            return [matrix[r][c-1]] + matrix[r-1][c-1:c+1]
        if is_top:
            return [matrix[r][c-1]] + [matrix[r][c+1]] + matrix[r+1][c-1:c+2]
        if is_left:
            return matrix[r-1][c:c+2] + [matrix[r][c+1]] + matrix[r+1][c:c+2]
        if is_right:
            return matrix[r-1][c-1:c+1] + [matrix[r][c-1]] + matrix[r+1][c-1:c+1]
        if is_bottom:
            return matrix[r-1][c-1:c+2] + [matrix[r][c-1]] + [matrix[r][c+1]]


    # Main Loop
    for row, row_values in enumerate(matrix):
        new_row = []
        for col, cell_value in enumerate(row_values):
            live_neighbors = sum(get_neighbor_view(row, col))
            if live_neighbors == 3 or cell_value and live_neighbors == 2:
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result