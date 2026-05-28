def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find the fewest number of coins needed to make the target amount of change.
    
    :param coins: List of coin denominations, always sorted.
    :param target: Target amount of change.
    :return: The shortest, sorted list of coins that sum to the target amount.
    :raises ValueError: If the target is negative or can"t be made with given coins.
    """

    # early return conditions
    if target == 0: 
        return []
    if target in coins: 
        return [target]

    # error handling
    if target < 0:
        raise ValueError("target can't be negative")
    if target < coins[0]:
        raise ValueError("can't make target with given coins")

    # initialize memoization table
    coins_to_make = [None] * (target+1)

    #bottom up approach
    for amount in range(1, target + 1):
        if amount in coins:
            coins_to_make[amount] = [amount]
            continue
        for coin in coins:
            if (difference := amount - coin) < 0: 
                break
            if coins_to_make[difference] is not None:
                if coins_to_make[amount] is None:
                    coins_to_make[amount] = coins_to_make[difference] + [coin]
                else:
                    coins_to_make[amount] = min(
                        coins_to_make[amount],
                        coins_to_make[difference] + [coin],
                        key=len
                    )

    # check if change was possible and return the sorted list
    if coins_to_make[target] is None:
        raise ValueError("can't make target with given coins")
    return sorted(coins_to_make[target])