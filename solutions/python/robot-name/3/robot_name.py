from string import digits, ascii_uppercase

LETTERS = {a+b for a in ascii_uppercase for b in ascii_uppercase}
NUMBERS = {x+y+z for x in str(digits) for y in str(digits) for z in str(digits)}
NAMES = iter({l+n for l in LETTERS for n in NUMBERS})

class Robot:    
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(NAMES)
        return self.name
