from enum import auto

SUBLIST = auto()
SUPERLIST = auto()
EQUAL = auto()
UNEQUAL = auto()


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
   
    if len(list_one) > len(list_two): longer, shorter, a = list_one, list_two, SUPERLIST
    else: shorter, longer, a = list_one, list_two, SUBLIST

    for i in range(len(longer)-len(shorter)+1):
        if longer[i:i+len(shorter)] == shorter:
            return a
    return UNEQUAL
    