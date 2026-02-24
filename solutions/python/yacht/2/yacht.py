def number_score(n): return lambda dice: sum(d for d in dice if d==n)
    
def YACHT(dice):return 50 if len(set(dice)) == 1 else 0
ONES = number_score(1)
TWOS = number_score(2)
THREES = number_score(3)
FOURS = number_score(4)
FIVES = number_score(5)
SIXES = number_score(6)
def FULL_HOUSE(dice):return sum(dice) if len(set(dice))==2 and dice.count(dice[2]) in [2,3] else 0
def FOUR_OF_A_KIND(dice):return 4*dice[3] if dice[0]==dice[3] or dice[1]==dice[4] else 0
def LITTLE_STRAIGHT(dice):return 30 if dice == [1,2,3,4,5] else 0
def BIG_STRAIGHT(dice):return 30 if dice == [2,3,4,5,6] else 0
CHOICE = sum


def score(dice, category):
    dice.sort()
    return category(dice)
