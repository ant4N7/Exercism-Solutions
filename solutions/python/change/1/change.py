from typing import List

def find_fewest_coins(coins: List[int], target: int) -> List[int]:
    """
    find the fewest number of coins needed to make the target amount of change
    
    :param coins: List of coin denominations, always sorted.
    :param target: Target amount of change.
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

    # initialize memoization
    change_list = [None] * (target+1)

    for amount in range(1,target+1):
        if amount in coins: 
            change_list[amount] = [amount]
            continue
        for coin in coins:
            if amount-coin < 0: break
            if change_list[amount-coin] is not None: # skip the amount if we cant make change for it
                if change_list[amount] is None: # if this is the first coin we've checked
                    change_list[amount] = change_list[amount-coin] + [coin]
                else: # if we already have a value, compare the len 
                    change_list[amount] = min(change_list[amount],change_list[amount-coin] + [coin],key=len)

    # check if change was possible and return the sorted list
    if change_list[target] is None:
        raise ValueError('can\'t make target with given coins')
    return sorted(change_list[target])
