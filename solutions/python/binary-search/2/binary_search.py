def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    result = search_list.copy()
    result.sort()
    while len(result) != 1:
        middle_element = result[len(result)//2]
        right_half = result[(len(result)//2)+1:]
        left_half = result[:(len(result)//2)]
        if middle_element == value:
            result = [middle_element]
        if middle_element > value:
            result = left_half
        if middle_element < value:
            result = right_half
    return search_list.index(*result)
    