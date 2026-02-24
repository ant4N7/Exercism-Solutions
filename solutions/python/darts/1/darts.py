def score(x, y):
    scores = [10, 5, 1, 0]
    hit = x**2 + y**2
    if hit <= 1:
        return 10
    if 1 < hit <= 25:
        return 5
    if 25 < hit <= 100:
        return 1
    return 0


"""
Bullseye:
    x**2 + y**2 <= 1
5 pts:
    x**2 + y**2 > 1
    x**2 + y**2 <= 25
    or
    1 < x**2 + y**2 <=25
1 pt:
    x**2 + y**2 > 25
    x**2 + y**2 <= 100
    or
    25 < x**2 + y**2 <= 100
outside the target:
    x**2 + y**2 > 100
"""