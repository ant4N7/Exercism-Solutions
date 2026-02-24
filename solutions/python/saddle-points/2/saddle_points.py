def saddle_points(matrix):
    if not matrix or not matrix[0]:
        return []
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')

    columns = list(zip(*matrix))
    
    return [
        {'row': i+1, 'column': j+1}
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
        if value == max(row) and value == min(columns[j])
    ]