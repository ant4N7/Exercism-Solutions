def rows(row_count, acc = []):
    if row_count < 0: raise ValueError('number of rows is negative')
    if not row_count: return acc
    if not acc: 
        acc = [[1]]
        return rows(row_count-1,acc)
    
    last_row = acc[-1]
    parity = len(last_row)
    last_row = last_row[:parity//2+1]
    next_row = [1]
    for a,b in zip(last_row,last_row[1:]):
        next_row.append(a+b)
    
    if parity%2:
        next_row = next_row + next_row[::-1]
    else:
        next_row = next_row + next_row[-2::-1]

    acc.append(next_row)

    return rows(row_count-1,acc)
