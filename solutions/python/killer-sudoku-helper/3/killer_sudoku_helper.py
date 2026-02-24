from typing import List
from itertools import combinations as combo


def combinations(target: int, size: int, exclude: List[int]) -> List[List[int]]:
    """generate the possible combinations for a killer sudoku cage"""

    # early return condition
    if size == 1: return [[target]]
    
    return [list(combination) for combination in combo(range(1,10),size)
            if len(combination) == len(set(combination))
            and sum(combination) == target
            and not any(digit in combination for digit in exclude)]
