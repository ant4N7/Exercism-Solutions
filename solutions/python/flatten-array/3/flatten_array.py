def flatten(iterable):
    flat_list = []
    stack = iterable[::-1]
    
    while stack:
        element = stack.pop()
        if type(element) == list:
            stack += element[::-1]
        elif element is not None:
            flat_list.append(element)
    
    return flat_list
    