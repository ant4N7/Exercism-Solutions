"""submitted via Exercism CLI"""

import numpy as np

def tick(matrix):
    if not matrix:
        return matrix
    
    grid = np.array(matrix)
    
    # Count neighbors using array slicing
    neighbors = (
        np.pad(grid, 1, mode='constant')[:-2, :-2] +  # top-left
        np.pad(grid, 1, mode='constant')[:-2, 1:-1] +  # top
        np.pad(grid, 1, mode='constant')[:-2, 2:] +    # top-right
        np.pad(grid, 1, mode='constant')[1:-1, :-2] +  # left
        np.pad(grid, 1, mode='constant')[1:-1, 2:] +   # right
        np.pad(grid, 1, mode='constant')[2:, :-2] +    # bottom-left
        np.pad(grid, 1, mode='constant')[2:, 1:-1] +   # bottom
        np.pad(grid, 1, mode='constant')[2:, 2:]       # bottom-right
    )
    
    # Apply Conway's rules
    result = ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) | (neighbors == 3)
    
    return result.astype(int).tolist()