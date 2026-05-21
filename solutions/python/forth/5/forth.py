from __future__ import annotations
import collections


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class Forth:
    """Forth object has 4 interconnected cores:
            The Tokenizer: a function that chops strings into words to be added or executed on the stack
            The Interpreter: a function that decides what to do with a token
            The Dictionary: a mapping of words to primitives or lists of other words
            The stack: the result of executing all tokens"""

    def __init__(self):
        self.input_log = []
        self.compiling = False
        self.new_word = None
        self.new_definition = None
        self.dictionary = self._load_defaults()
        self.stack = []

    def tokenizer(self, raw_input: str):
        self.input_log.append(raw_input)
        for token in raw_input.upper().split():
            if self.compiling:
                self.compiler(token)
            else:
                self.interpreter(token)

    def interpreter(self, token: str):
        # : or int or in self.dictionary
        if token == ':':
            self.compiling = True
        elif token in self.dictionary:
            if isinstance(self.dictionary[token], list):
                for sub_token in self.dictionary[token]:
                    self.interpreter(sub_token)
            else:
                try:
                    self.dictionary[token](self)
                except IndexError as e:
                    raise StackUnderflowError('Insufficient number of items in stack') from e
        else:
            try:
                self.stack.append(int(token))
            except ValueError as e:
                raise ValueError('undefined operation') from e

    def compiler(self, token: str):
        if token == ';':
            self.dictionary[self.new_word] = self.new_definition
            self.compiling = False
            self.new_word = None
            self.new_definition = None
        elif self.new_word is not None:
            # case where user defined word is using a word with the same name
            if token in self.dictionary and token not in '+-*/DUPDROPSWAPOVER':
                self.new_definition.extend(self.dictionary[token])
            else:
                self.new_definition.append(token)
        else:
            try:
                int(token)
                # If we get here, token is a valid integer - this is illegal
                raise ValueError('illegal operation')
            except ValueError as e:
                # Check if this is our custom error or int() conversion failure
                if str(e) == 'illegal operation':
                    raise  # Re-raise our custom error
                # If int() failed, token is not an integer - proceed normally
                self.new_word = token
                self.new_definition = []

    @staticmethod
    def _load_defaults() -> dict[str, collections.abc.Callable]:
        def divide(obj: Forth):
            denominator, numerator = obj.stack.pop(), obj.stack.pop()
            if denominator == 0:
                raise ZeroDivisionError('divide by zero')
            obj.stack.append(numerator // denominator)

        def swap(obj: Forth):
            a, b = obj.stack.pop(), obj.stack.pop()
            obj.stack.extend([a, b])

        def over(obj: Forth):
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

def evaluate(input_data: list[str]) -> list[int]:
    forth_object = Forth()
    for raw_input in input_data:
        forth_object.tokenizer(raw_input)
    return forth_object.stack