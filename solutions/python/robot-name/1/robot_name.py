from random import choices
from string import digits, ascii_uppercase as letters


class Robot:
    existing_names = set()
    
    def __init__(self):
        self.reset()

    def reset(self):
        while True:
            name = ''.join(choices(letters,k=2))+''.join(choices(digits,k=3))
            if name not in self.existing_names:
                self.name = name
                self.existing_names.add(name)
                break
        return self
