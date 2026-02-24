def is_triangle(sides):
    a, b, c = sides
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif 0 in sides:
        return False
    else:
        return True

def equilateral(sides):
    return len(set(sides)) == 1 if is_triangle(sides) else False
    

def isosceles(sides):
    return len(set(sides)) < 3 if is_triangle(sides) else False


def scalene(sides):
    return len(set(sides)) == 3 if is_triangle(sides) else False