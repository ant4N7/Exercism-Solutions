def annotate(minefield: list[str]) -> list[str]:
    """add numbers to a minefield based on mine proximity count"""

    # validate inputs
    if (any(len(l1) != len(l2) for l1,l2 in zip(minefield,minefield[1:])) or
        any(char not in ' *' for line in minefield for char in line)):
        raise ValueError('The board is invalid with current input.')

    # get the row and column for each mine
    mine_coords = [(r,c) 
                   for r,line in enumerate(minefield) 
                   for c,char in enumerate(line) 
                   if char == '*']
    
    # generate the proximity coordinates
    proximity_coords = []
    for coord in mine_coords:
        r,c = coord
        proximity_coords.extend([(r-1,c-1),(r-1,c),(r-1,c+1),
                                 (r,c-1),          (r,c+1),
                                 (r+1,c-1),(r+1,c),(r+1,c+1)])

    # map proximity coordinates to their counts
    proximity_map = {item:str(proximity_coords.count(item)) for item in set(proximity_coords)}
    
    # put the mines in the mapping
    for coord in mine_coords:
        proximity_map[coord] = '*'
    
    # main logic
    output = []
    for r in range(len(minefield)):
        row = ''
        for c in range(len(minefield[0])):
            row += proximity_map.get((r,c),' ')
        output.append(row)
    return output
