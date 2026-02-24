from typing import List

def find_fewest_coins(coins: List[int], target: int) -> List[int]:
    """
    find the fewest number of coins needed to make the target val of change
    
    :param coins: List of coin denominations, always sorted.
    :param target: Target val of change.
    :return: Sorted list of coins that sum to the target with the fewest coins.
    :raises ValueError: If the target is negative or can't be made with given coins.
    """

    # early return conditions
    if target == 0: return []
    if target in coins: return [target]

    # error handling
    if target < 0:
        raise ValueError('target can\'t be negative')
    if target < coins[0]:
        raise ValueError('can\'t make target with given coins')

    # initialize memoization table
    change_list = [None] * (target+1)

    #bottom up approach
    for val in range(1,target+1):
        if val in coins: 
            change_list[val] = [val]
            continue
        for coin in coins:
            if val-coin < 0: break
            if change_list[val-coin] is not None:
                if change_list[val] is None:
                    change_list[val] = change_list[val-coin] + [coin]
                else: change_list[val] = min(change_list[val],change_list[val-coin] + [coin],key=len)

    # check if change was possible and return the sorted list
    if change_list[target] is None:
        raise ValueError('can\'t make target with given coins')
    return sorted(change_list[target])
