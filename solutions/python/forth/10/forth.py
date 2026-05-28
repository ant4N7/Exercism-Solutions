from __future__ import annotations
import collections

# Minimum stack size for these operators.
# Anything smaller triggers a StackUnderflowError.
STACK_OPS: dict[int, list[str]] = {
    0: [":"],
    1: ["DUP", "DROP"],
    2: ["+", "-", "*", "/", "SWAP", "OVER"],
}
MIN_STACK: dict[str,int] = {
    op: count for count, ops in STACK_OPS.items() for op in ops
}

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

    def tokenizer(self, raw_input: str) -> None:
        tokens = raw_input.upper().split()
        if tokens and tokens[0] == ':':
            self.compiler(tokens)
        else:
            for token in tokens:
                self.interpreter(token)

    def compiler(self, tokens: list[str]) -> None:
        """The compiler processes the whole ': new-word new-def ;' phrase at once."""
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
    
    def interpreter(self, token: str) -> None:
        if token in self.dictionary:
            # handle user defined words
            if isinstance(self.dictionary[token], list):
                for sub_token in self.dictionary[token]:
                    self.interpreter(sub_token)
            # handle defualt words
            elif len(self.stack) < MIN_STACK[token]:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                self.dictionary[token](self)
        elif not self._is_numeric(token):
            raise ValueError('undefined operation')
        else: # push numbers to the stack
            self.stack.append(int(token))

    @staticmethod
    def _is_numeric(token: str) -> bool:
        """Expands the default behavior of isnumeric() to catch numbers prefixed with a sign."""
        if not token:
            return False
        if len(token) > 1 and token[0] in '-+':
            return token[1:].isnumeric()
        return token.isnumeric()
    
    @staticmethod
    def _load_defaults() -> dict[str, collections.abc.Callable]:
        """Builds the defualt Forth dictionary."""
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