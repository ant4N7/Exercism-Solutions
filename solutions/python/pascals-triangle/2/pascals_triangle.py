from math import comb

def rows(row_count, acc = []):
    if row_count < 0: raise ValueError('number of rows is negative')
    if row_count == 0: return acc[::-1]
    if not acc: acc = []
    acc.append([comb(row_count-1,k) for k in range(row_count)])
    return rows(row_count-1, acc)
    