def numberOfWaysToTraverseGraph(width, height):
    matrix = []
    
    for i in range(height):
        matrix.append(([0] * width)[:])
        
    for i in range(height):
        matrix[i][0] = 1
        
    for j in range(width):
        matrix[0][j] = 1
        
    for i in range(1, height):
        for j in range(1, width):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    
    return matrix[-1][-1]
