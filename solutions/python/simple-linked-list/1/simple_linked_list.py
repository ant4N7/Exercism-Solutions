class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self.length = 0

        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self.length

    def head(self):
        if self._head: return self._head
        raise EmptyListException("The list is empty.")

    def push(self, value):
        self.length += 1
        if not self._head:
            self._head = Node(value)
            return
        new_node = Node(value,self._head)
        self._head = new_node

    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        self.length -= 1
        val = self._head.value()
        self._head = self._head.next()
        return val

    def reversed(self):
        return reversed(list(self))
