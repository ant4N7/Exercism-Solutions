from string import ascii_lowercase as a
from secrets import choice
from itertools import cycle

class Cipher:
    def __init__(self, key=None):
        if key: self.key = key
        else: self.key = ''.join(choice(a)for _ in range(100))

    def encode(self, text):
        key = cycle(self.key)
        return ''.join(a[(a.index(ch)+a.index(next(key)))%26] for ch in text)

    def decode(self, text):
        key = cycle(self.key)
        return ''.join(a[(a.index(ch)-a.index(next(key)))%26] for ch in text)
