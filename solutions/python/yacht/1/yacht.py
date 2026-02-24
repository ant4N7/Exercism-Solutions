# Score categories.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(pips for pips in dice if pips == 1)
TWOS = lambda dice: sum(pips for pips in dice if pips == 2)
THREES = lambda dice: sum(pips for pips in dice if pips == 3)
FOURS = lambda dice: sum(pips for pips in dice if pips == 4)
FIVES = lambda dice: sum(pips for pips in dice if pips == 5)
SIXES = lambda dice: sum(pips for pips in dice if pips == 6)
FULL_HOUSE = lambda dice: sum(dice) if is_full_house(dice) else 0
FOUR_OF_A_KIND = lambda dice: sum(the_four(dice)) if is_four_of_a_kind(dice) else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)

def is_full_house(dice):
    unique = set(dice)
    if len(unique) != 2: return False
    return dice.count(unique.pop())==3 or dice.count(unique.pop())==3

def is_four_of_a_kind(dice):
    unique = set(dice)
    if len(unique) > 2: return False
    if len(unique) == 2:
        return dice.count(unique.pop())==4 or dice.count(unique.pop())==4
    return True

def the_four(dice):
    dice.sort()
    if dice[0] == dice[1]: return dice[:-1]
    return dice[1:]

def score(dice, category):
    return category(dice)
