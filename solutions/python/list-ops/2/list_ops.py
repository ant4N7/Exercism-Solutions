def append(list1, list2):
    return list1 + list2


def concat(lists):
    if length(lists) > 1:
        head = lists[0]
        tail = lists[1:]
    elif length(lists) == 1:
        head = lists[0]
        tail = []
    else:
        return []

    return append(head, concat(tail))


def filter(function, list):
    if length(list) > 1:
        head = list[0]
        tail = list[1:]
    elif length(list) == 1:
        head = list[0]
        tail = []
    else:
        return []
        
    return append([head], filter(function, tail)) if function(head) else append([], filter(function, tail))


def length(list):
    counter = 0
    for _ in list:
        counter += 1
    return counter


def map(function, list):
    if length(list) > 1:
        head = list[0]
        tail = list[1:]
    elif length(list) == 1:
        head = list[0]
        tail = []
    else:
        return []

    return append([function(head)], map(function, tail))


def foldl(function, list, initial):
    if length(list) > 1:
        head = list[0]
        tail = list[1:]
    elif length(list) == 1:
        head = list[0]
        tail = []
    else:
        return initial

    return foldl(function, tail, function(initial, head))


def foldr(function, list, initial):
    if length(list) > 1:
        head = list[0]
        tail = list[1:]
    elif length(list) == 1:
        head = list[0]
        tail = []
    else:
        return initial

    return function(foldr(function, tail, initial), head)


def reverse(list):
    if length(list) > 1:
        head = list[0]
        tail = list[1:]
    elif length(list) == 1:
        head = list[0]
        tail = []
    else:
        return []

    return append(reverse(tail), [head])
