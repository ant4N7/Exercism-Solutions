def score(x, y):
    hit = x**2 + y**2
    return (hit <= 1) * 5 + (hit <= 25) * 4 + (hit <= 100)
    