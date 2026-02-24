def append(list1, list2):
    return list1 + list2


def concat(lists):
    return sum((el for el in lists), [])


def filter(function, list):
    return [el for el in list if function(el)]


def length(list):
    length = 0
    for el in list:
        length += 1
    return length


def map(function, list):
    return [function(el) for el in list]


def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc


def foldr(function, list, initial):
    acc = initial
    list = list[::-1]
    for el in list:
        acc = function(acc, el)
    return acc


def reverse(list):
    return list[::-1]
