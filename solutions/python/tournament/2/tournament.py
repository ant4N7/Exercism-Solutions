def tally(rows):
    data = sorted(extract(rows).items(), key = lambda x: (-x[1][0],-x[1][1]))
    return ['Team                           | MP |  W |  D |  L |  P'] + \
    [
        '{team:<31}|{mp:>3} |{w:>3} |{d:>3} |{l:>3} |{p:>3}'.format(
            team = point[0],
            mp = sum(point[1]),
            w = point[1][0],
            d = point[1][1],
            l = point[1][2],
            p = 3*point[1][0] + point[1][1]
        )
        for point in data
    ]
    

def extract(rows: list[str,]) -> dict[str:list[int]]:
    """takes the list of strings as input and returns a dictionary
    with team names as the keys and a list of three ints representing
    wins, draws, and losses as the values"""
    result = {}
    while rows:
        point = rows.pop()
        split = point.split(';')
        team1,team2,outcome = split
        # key, value pairs -> team:[w,d,l]
        result.setdefault(team1,[0,0,0])
        result.setdefault(team2,[0,0,0])
        if outcome == "win":
            result[team1][0] += 1
            result[team2][2] += 1
        elif outcome == "draw":
            result[team1][1] += 1
            result[team2][1] += 1
        elif outcome == "loss":
            result[team1][2] += 1
            result[team2][0] += 1
    return result
