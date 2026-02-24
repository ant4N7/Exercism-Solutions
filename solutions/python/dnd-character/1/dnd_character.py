from random import choices as roll
d6 = (1,2,3,4,5,6)

class Character:    
    def __init__(self):
        self.strength     = self.ability()
        self.dexterity    = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom       = self.ability()
        self.charisma     = self.ability()
        self.hitpoints    = 10 + modifier(self.constitution)

    @staticmethod
    def roll_4d6():
        multiset = roll(d6,k=4)
        multiset.sort(reverse=True)
        return multiset

    def ability(self):
        return sum(self.roll_4d6()[:3])

def modifier(value):
    return (value-10)//2
