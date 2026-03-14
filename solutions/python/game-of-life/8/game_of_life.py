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

    # Main Loop
    for row, row_values in enumerate(matrix):
        new_row = []
        for col, cell_value in enumerate(row_values):
            live_neighbors = sum(1 for delta_row, delta_col in NEIGHBOR_OFFSETS \
                                    if 0 <= row + delta_row < height \
                                    and 0 <= col + delta_col < width\
                                    and matrix[row + delta_row][col + delta_col])
            if live_neighbors == 3 or (cell_value and live_neighbors == 2):
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result