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
    def __init__(self, values=[]):
        self._head = None
        self._length = 0
        for value in values:
            self.push(value)
            
    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()
            
    def __len__(self):
        return self._length
        
    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head
        
    def push(self, value):
        self._length += 1
        new_node = Node(value, self._head)
        self._head = new_node
        
    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
            
        self._length -= 1
        value = self._head.value()
        self._head = self._head.next()
        return value
        
    def reversed(self):
        return LinkedList(list(self))