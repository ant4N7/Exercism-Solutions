def flatten(iterable):
    if len(iterable) == 0:
        return iterable
    flat_list = []
    for element in iterable:
        if type(element) == list:
            flat_list.extend(flatten(element))
        elif element == None:
            continue
        else:
            flat_list.append(element)
    return flat_list
    