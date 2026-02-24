def is_triangle(sides):
    a, b, c = sides
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif 0 in sides:
        return False
    else:
        return True

def equilateral(sides):
    a, b, c = sides
    return a == b == c if is_triangle(sides) else False
    

def isosceles(sides):
    a, b, c = sides
    return a == b or a == c or b == c if is_triangle(sides) else False


def scalene(sides):
    a, b, c = sides
    return a != b != c != a if is_triangle(sides) else False