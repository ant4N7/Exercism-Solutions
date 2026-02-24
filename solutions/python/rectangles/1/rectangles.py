from itertools import combinations

def rectangles(strings):
    vertices = [(c,r) for r,row in enumerate(strings) for c,col in enumerate(row) if col=='+']
    pipes = [(c,r) for r,row in enumerate(strings) for c,col in enumerate(row) if col=='|' or col =='+']
    dashes = [(c,r) for r,row in enumerate(strings) for c,col in enumerate(row) if col=='-' or col =='+']
    
    # early return condition
    if len(vertices) < 4: return 0

    point_combinations = combinations(vertices, 4)
    return sum(is_rectangle(point_combination,pipes,dashes) for point_combination in point_combinations)

def is_rectangle(point_combination,pipes,dashes):
    x1,y1 = point_combination[0][0], point_combination[0][1]
    x2,y2 = point_combination[1][0], point_combination[1][1]
    x3,y3 = point_combination[2][0], point_combination[2][1]
    x4,y4 = point_combination[3][0], point_combination[3][1]
    
    points_check = (x1 == x3 and x2 == x4 and y1 == y2 and y3 == y4) 
    pipes_check = all((x1,y) in pipes and (x2,y) in pipes for y in range(y1+1,y3))
    dashes_check = all((x,y1) in dashes and (x,y3) in dashes for x in range(x1+1,x2))

    
    return points_check and pipes_check and dashes_check
