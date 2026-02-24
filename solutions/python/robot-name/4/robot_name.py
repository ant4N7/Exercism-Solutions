from string import digits, ascii_uppercase

LETTERS = (a+b for a in ascii_uppercase for b in ascii_uppercase)
NUMBERS = (str(i).zfill(3) for i in range(1000))
NAMES = iter({l+n for l in LETTERS for n in NUMBERS})

class Robot:    
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(NAMES)
        return self.name
