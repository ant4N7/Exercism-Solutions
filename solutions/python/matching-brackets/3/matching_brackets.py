def is_paired(input_string):
    clopen = str.maketrans(')}]','({[')
    stack = []
    for char in input_string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or char.translate(clopen) != stack.pop():
                return False
    return not stack
