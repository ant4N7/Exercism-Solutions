from __future__ import annotations
import collections


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""

class Forth:
    """Forth object has 5 interconnected cores:
        The Tokenizer: a function that chops strings into words to be added or executed on the stack
        The Interpreter: a function that decides what to do with a token
        The Compiler: a function that handles word definitions
        The Dictionary: a mapping of words to primitives or lists of other words
        The stack: the result of executing all tokens"""

    def __init__(self):
        self.dictionary = self._load_defaults()
        self.stack = []

    def tokenizer(self, raw_input: str):
        tokens = raw_input.upper().split()
        if tokens and tokens[0] == ':':
            self.compiler(tokens)
        else:
            for token in tokens:
                self.interpreter(token)

    def compiler(self, tokens):
        """The new compiler.
        This version processes the whole : ; phrase at once"""
        new_word, *new_definition = tokens[1:-1]
        if new_word.isnumeric() or (len(new_word) > 1 and new_word[1:].isnumeric()):
            raise ValueError('illegal operation')
        
        # Find indices where user-defined words are used
        user_defined_indices = tuple(
            i for i, x in enumerate(new_definition) 
            if x in self.dictionary and isinstance(self.dictionary[x], list)
        )
        
        # Replace each user-defined word with its definition
        for j in user_defined_indices:
            new_definition[j:j+1] = self.dictionary[new_definition[j]]
        
        self.dictionary[new_word] = new_definition
    
    def interpreter(self, token: str):
        if token in self.dictionary:
            if isinstance(self.dictionary[token], list):
                for sub_token in self.dictionary[token]:
                    self.interpreter(sub_token)
            else:
                try:
                    self.dictionary[token](self)
                except IndexError:
                    raise StackUnderflowError('Insufficient number of items in stack')
        else:
            try:
                self.stack.append(int(token))
            except ValueError:
                raise ValueError('undefined operation')

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
            '/': divide,
            'DUP': lambda obj: obj.stack.extend([obj.stack.pop()]*2),
            'DROP': lambda obj: obj.stack.pop(),
            'SWAP': swap,
            'OVER': over,
        }

def evaluate(input_data: list[str]) -> list[int]:
    forth = Forth()
    for raw_input in input_data:
        forth.tokenizer(raw_input)
    return forth.stack