def encode(numbers):
    bytes_ = []
    
    for number in numbers:
        if number == 0: bytes_.append(0)
        
        result = []
        while number > 0:
            byte = number & 0b01111111
            number >>= 7
            if result:
                byte |= 0b10000000
            result.insert(0, byte)
        bytes_.extend(result)

    return bytes_


def decode(bytes_):

    byte = 0
    numbers = []
    
    for b in bytes_:
        byte |= b & 0b01111111
        
        if b & 0b10000000:
            byte <<= 7
        else:
            numbers.append(byte)
            byte = 0

    if numbers: return numbers
    raise ValueError('incomplete sequence')
