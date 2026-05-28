from __future__ import annotations
import collections


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""


class Forth:
    """A Forth interpreter implementation.

    The interpreter consists of five interconnected components:
    - Tokenizer: Splits input strings into words for processing
    - Interpreter: Determines how to handle each token (execute, push, or recurse)
    - Compiler: Processes word definitions (": word-name definition ;")
    - Dictionary: Maps word names to either callable primitives or lists of tokens
    - Stack: Stores integer values resulting from token execution
    """
    
    # Minimum stack size for these operators.
    # Anything smaller triggers a StackUnderflowError.
    STACK_OPS = {
        0: [":"],
        1: ["DUP", "DROP"],
        2: ["+", "-", "*", "/", "SWAP", "OVER"],
    }
    MIN_STACK = {
        op: count for count, ops in STACK_OPS.items() for op in ops
    }
    
    def __init__(self, input_data=None):
        self.dictionary = self._load_defaults()
        self.stack = []
        if input_data:
            for raw_input in input_data:
                self.tokenizer(raw_input)

    def tokenizer(self, raw_input: str) -> None:
        tokens = raw_input.upper().split()
        if tokens and tokens[0] == ":":
            self.compiler(tokens)
        else:
            for token in tokens:
                self.interpreter(token)

    def compiler(self, tokens: list[str]) -> None:
        new_word, *new_definition = tokens[1:-1]
        if self._is_numeric(new_word):
            raise ValueError("illegal operation")
        
        def translate_word(word):
            return (
                self.dictionary[word]
                if word in self.dictionary and isinstance(self.dictionary[word], list)
                else [word]
            )
        
        translated_definition = [
            item
            for word in new_definition
            for item in translate_word(word)
        ]
        self.dictionary[new_word] = translated_definition
    
    def interpreter(self, token: str) -> None:
        if token in self.dictionary:
            # handle user defined words
            if isinstance(self.dictionary[token], list):
                for sub_token in self.dictionary[token]:
                    self.interpreter(sub_token)
            # handle defualt words
            elif len(self.stack) < self.MIN_STACK[token]:
                raise StackUnderflowError("Insufficient number of items in stack")
            else:
                self.dictionary[token](self)
        elif not self._is_numeric(token):
            raise ValueError("undefined operation")
        else: # push numbers to the stack
            self.stack.append(int(token))

    @staticmethod
    def _is_numeric(token: str) -> bool:
        """Expands the default behavior of isnumeric() to catch numbers prefixed with a sign."""
        if not token:
            return False
        if len(token) > 1 and token[0] in "-+":
            return token[1:].isnumeric()
        return token.isnumeric()
    
    @staticmethod
    def _load_defaults() -> dict[str, collections.abc.Callable]:
        """Builds the defualt Forth dictionary."""
        def divide(obj: Forth) -> None:
            denominator, numerator = obj.stack.pop(), obj.stack.pop()
            if denominator == 0:
                raise ZeroDivisionError("divide by zero")
            obj.stack.append(numerator // denominator)

        def swap(obj: Forth) -> None:
            a, b = obj.stack.pop(), obj.stack.pop()
            obj.stack.extend([a, b])

        def over(obj: Forth) -> None:
            a, b = obj.stack.pop(), obj.stack.pop()
            obj.stack.extend([b, a, b])

        return {
            "+": lambda obj: obj.stack.append(obj.stack.pop() + obj.stack.pop()),
            "-": lambda obj: obj.stack.append(-obj.stack.pop() + obj.stack.pop()),
            "*": lambda obj: obj.stack.append(obj.stack.pop() * obj.stack.pop()),
            "/": divide,
            "DUP": lambda obj: obj.stack.extend([obj.stack.pop()]*2),
            "DROP": lambda obj: obj.stack.pop(),
            "SWAP": swap,
            "OVER": over,
        }


def evaluate(input_data: list[str]) -> list[int]:
    return Forth(input_data).stack