def score(x, y):
    hit = x**2 + y**2
    if hit <= 1: return 10        
    if 1 < hit <= 25: return 5        
    if 25 < hit <= 100: return 1        
    return 0
    