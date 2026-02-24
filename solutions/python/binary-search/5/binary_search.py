def find(search_list, value):
    lo = 0
    hi = len(search_list)
    while hi-lo > 1:
        mid = lo + (hi-lo)//2
        if search_list[mid] == value:
            return mid
        if search_list[mid] > value:
            hi = mid
        if search_list[mid] < value:
            lo = mid
    if len(search_list) == 0 or search_list[lo] != value:
        raise ValueError("value not in array")
    return lo
