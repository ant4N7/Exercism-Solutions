from typing import List
from itertools import combinations as combo

ONLY_ONE_COMBO = {
    2:{3:[1,2],4:[1,3],17:[8,9],16:[7,9]},
    3:{6:[1,2,3],7:[1,2,4],24:[7,8,9],23:[6,8,9]},
    4:{10:[1,2,3,4],11:[1,2,3,5],30:[6,7,8,9],29:[5,7,8,9]},
    5:{15:[1,2,3,4,5],16:[1,2,3,4,6],35:[5,6,7,8,9],34:[4,6,7,8,9]},
    6:{21:[1,2,3,4,5,6],22:[1,2,3,4,5,7],39:[4,5,6,7,8,9],38:[3,5,6,7,8,9]},
    7:{28:[1,2,3,4,5,6,7],29:[1,2,3,4,5,6,8],42:[3,4,5,6,7,8,9],41:[2,4,5,6,7,8,9]},
    8:{
        36:[1,2,3,4,5,6,7,8],
        37:[1,2,3,4,5,6,7,9],
        38:[1,2,3,4,5,6,8,9],
        39:[1,2,3,4,5,7,8,9],
        40:[1,2,3,4,6,7,8,9],
        41:[1,2,3,5,6,7,8,9],
        42:[1,2,4,5,6,7,8,9],
        43:[1,3,4,5,6,7,8,9],
        44:[2,3,4,5,6,7,8,9]
    },
    9:{45:[1,2,3,4,5,6,7,8,9]}
}

def combinations(target: int, size: int, exclude: List[int]) -> List[List[int]]:
    """generate the possible combinations for a killer sudoku cage"""

    # early return conditions
    if size == 1:
        return [[target]]
    if ONLY_ONE_COMBO[size].get(target,0):
        return [ONLY_ONE_COMBO[size][target]]

    #use itertools
    return [list(combination) for combination in combo(range(1,10),size)
            if len(combination) == len(set(combination))
            and sum(combination) == target
            and not any(digit in combination for digit in exclude)]
