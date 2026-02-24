class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)
        else: raise BufferEmptyException('Circular buffer is empty')

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else: raise BufferFullException('Circular buffer is full')

    def overwrite(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            self.buffer.pop(0)
            self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
