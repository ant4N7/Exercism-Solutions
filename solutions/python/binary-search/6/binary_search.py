def find(search_list, value):
    lo = 0
    hi = len(search_list) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1

    raise ValueError("value not in array")