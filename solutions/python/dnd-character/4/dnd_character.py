from random import seed,choices as roll
d6 = (1,2,3,4,5,6)
ABILITIES = ('strength','dexterity','constitution',
             'intelligence','wisdom','charisma')

class Character:   
    seed()
    def __init__(self):
        for ability in ABILITIES:
            setattr(self,ability,self.ability())
        self.hitpoints    = 10 + modifier(self.constitution)    

    @staticmethod
    def ability():
        return sum(roll_4d6()[:3])

def modifier(value):
    return (value-10)//2

def roll_4d6():
    multiset = roll(d6,k=4)
    multiset.sort(reverse=True)
    return multiset
