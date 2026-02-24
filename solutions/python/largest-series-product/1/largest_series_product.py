from collections import deque
from itertools import islice
from functools import reduce

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

def largest_product(series, size):
    
    # input validation
    if len(series) < size:# span of numbers is longer than number series
        raise ValueError("span must be smaller than string length")
    
    if size < 1:# span of number is negative
        raise ValueError("span must not be negative")
    
    if not series.isdigit():# series includes non-number input
        raise ValueError("digits input must only contain digits")

    answer = 0
    for chunk in sliding_window(series,size):
        temp = reduce(lambda x,y: int(x)*int(y),chunk)
        if temp > answer:
            answer = temp
    return answer
