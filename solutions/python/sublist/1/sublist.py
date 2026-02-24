"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        return list_one == list_two
   
    if len(list_one) > len(list_two): longer, shorter, a = list_one, list_two, 2
    else: shorter, longer, a = list_one, list_two, 3

    for i in range(len(longer)):
        if longer[i:i+len(shorter)] == shorter:
            return a
    return 0