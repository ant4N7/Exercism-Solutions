"""Game of Life"""
NEIGHBOR_OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """A function that takes a matrix of 0s and 1s representing the state of a Game of Life board, and returns a new matrix representing the state of the board after one tick. 
    The input matrix should not be modified."""
    
    # Early return for edge case
    if not matrix: 
        return matrix

    # initialize result matrix
    result = []

    # precompute height and width for bounds checking
    height, width = len(matrix), len(matrix[0])

    # Main Loop
    for row in range(height):
        result.append([])
        for col in range(width):
            live_neighbors = sum(1 for delta_row, delta_col in NEIGHBOR_OFFSETS if 0 <= row + delta_row < height and 0 <= col + delta_col < width and matrix[row + delta_row][col + delta_col])
            if (matrix[row][col] and 2 <= live_neighbors < 4) or (not matrix[row][col] and live_neighbors == 3):
                result[row].append(1)
            else:
                result[row].append(0)
    return result