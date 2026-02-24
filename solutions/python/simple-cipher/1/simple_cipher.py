from string import ascii_lowercase as alphabet
from secrets import choice

class Cipher:
    def __init__(self, key=None):
        if key: self.key = key
        else: self.key = ''.join(choice(alphabet)for _ in range(100))

    def encode(self, text):
        key = self.key*100
        return ''.join(alphabet[(alphabet.index(ch)+alphabet.index(key[i]))%26]\
                       for i,ch in enumerate(text))

    def decode(self, text):
        key = self.key*100
        return ''.join(alphabet[(alphabet.index(ch)-alphabet.index(key[i]))%26]\
                       for i,ch in enumerate(text))
