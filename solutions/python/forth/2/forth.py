from __future__ import annotations
import collections


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class Forth:
    def __init__(self):
        self.stack = []
        self.dictionary = Dictionary()
        self.editing = False
        self.new_word = None
        self.new_def = None
    
    def primed_token(self, number_str: str):
        def p(obj):
            obj.stack.append(int(number_str))
        return p

    def tokenize(self, data: str):
        for raw in data.upper().split(' '):
            if self.editing:
                # add word to dictionary
                if raw == ';':
                    #commit changes
                    self.dictionary.edit_lookup(self, self.new_word,self.new_def)
                    #reset flags
                    self.editing = False
                    self.new_word = None
                    self.new_def = None
                elif self.new_word:
                    self.new_def.append(raw)
                elif (len(raw) == 1 and raw.isnumeric()) or (len(raw) > 1 and raw[0] == '-' and raw[1:].isnumeric()):
                    raise ValueError('illegal operation')
                else:
                    self.new_word = raw
                    self.new_def = []
            elif raw == ':':
                self.editing = True
            elif raw in self.dictionary.lookup:
                try:
                    if isinstance(self.dictionary.lookup[raw], list):
                        for func in self.dictionary.lookup[raw]:
                            func(self)  # Execute immediately
                    else:
                        self.dictionary.lookup[raw](self)
                except IndexError as e:
                    raise StackUnderflowError('Insufficient number of items in stack') from e
            else:
                try:
                    self.stack.append(int(raw))
                except ValueError as e:
                    raise ValueError('undefined operation') from e

class Dictionary:
    def __init__(self):
        # keys are str : val is func or list[func,...]
        self.lookup = self._load_defaults()

    @staticmethod
    def _load_defaults() -> dict[str, collections.abc.Callable]:
        def divide(obj):
            denominator, numerator = obj.stack.pop(), obj.stack.pop()
            if denominator == 0:
                raise ZeroDivisionError('divide by zero')
            obj.stack.append(numerator // denominator)

        def swap(obj):
            a, b = obj.stack.pop(), obj.stack.pop()
            obj.stack.extend([a, b])

        def over(obj):
            a, b = obj.stack.pop(), obj.stack.pop()
            obj.stack.extend([b, a, b])

        return {
            '+': lambda obj: obj.stack.append(obj.stack.pop() + obj.stack.pop()),
            '-': lambda obj: obj.stack.append(-obj.stack.pop() + obj.stack.pop()),
            '*': lambda obj: obj.stack.append(obj.stack.pop() * obj.stack.pop()),
            '/': lambda obj: divide(obj),
            'DUP': lambda obj: obj.stack.extend([obj.stack.pop()]*2),
            'DROP': lambda obj: obj.stack.pop(),
            'SWAP': lambda obj: swap(obj),
            'OVER': lambda obj: over(obj),
        }
    
    def edit_lookup(self, f_obj: Forth, key: str, values: list[str]):
        """Edit or Commit a new entry in the Dictionary."""
        new_def = []
        for word in values: # iterate through the given definition
            if word in self.lookup:
                if isinstance(self.lookup[word], list): # this means its a user defined word
                    new_def.extend(self.lookup[word])
                else: # one of the defaults
                    new_def.append(self.lookup[word])                    
            else: # its a number
                new_def.append(f_obj.primed_token(word))
        self.lookup[key] = new_def


def evaluate(input_data):
    f_obj = Forth()
    for instructions in input_data:
        f_obj.tokenize(instructions)
    return f_obj.stack