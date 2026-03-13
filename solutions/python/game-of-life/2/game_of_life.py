from typing import List
from copy import deepcopy

def tick(matrix: List[List[int]]) -> List[List[int]]:
    """one tick of Conway's Game of Life does not modify input"""
    # Early return for edge case
    if not matrix: return matrix

    # preserve input
    result = deepcopy(matrix)

    def check_neighbors(row: int, col: int, matrix: List[List[int]]) -> int:
        """just reads from the matrix and counts live neighbors"""
        height, width = len(matrix), len(matrix[0])
        live_count = 0
        for delta_row, delta_col in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < height and 0 <= new_col < width and matrix[new_row][new_col]:
                live_count += 1
        return live_count

    # Main Loop
    for row, matrix_row in enumerate(matrix):
        for col, cell in enumerate(matrix_row):
            live_neighbors = check_neighbors(row, col, matrix)
            if cell and 2 <= live_neighbors < 4: continue
            if not cell and live_neighbors == 3:
                result[row][col] = 1
            else:
                result[row][col] = 0
    return result