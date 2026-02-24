def saddle_points(matrix):
    
    column = list((zip(*matrix)))

    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            try:
                if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(column[j]):
                    result.append({'row':i+1,'column':j+1})
            
            except: raise ValueError('irregular matrix')

    return result
