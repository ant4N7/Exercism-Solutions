from typing import List, Tuple
from copy import deepcopy

def tick(matrix: List[List[int]]) -> List[List[int]]:
    """one tick of Conway's Game of Life does not modify input"""
    # Early return for edge case
    if not matrix: return matrix

    # preserve input
    result = deepcopy(matrix)

    def check_neighbors(r: int, c: int, matrix: List[List[int]]) -> int:
        """just reads from the matrix and counts live neighbors"""
        height, width = len(matrix), len(matrix[0])
        live_count = 0
        for dr, dc in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and matrix[nr][nc]:
                live_count += 1
        return live_count

    # Main Loop
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            live_neighbors = check_neighbors(r, c, matrix)
            if cell and 2 <= live_neighbors < 4: 
                continue
            elif not cell and live_neighbors == 3:
                result[r][c] = 1
            else:
                result[r][c] = 0
    return result

