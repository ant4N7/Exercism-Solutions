def equilateral(sides):
    a, b, c = sides
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif 0 in sides:
        return False
    else:
        return a == b == c
    

def isosceles(sides):
    a, b, c = sides
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif 0 in sides:
        return False
    else:
        return a == b or a == c or b == c


def scalene(sides):
    a, b, c = sides
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif 0 in sides:
        return False
    else:
        return a != b != c != a