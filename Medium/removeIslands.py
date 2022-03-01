def removeIslands(matrix):
    if (len(matrix) < 2) or (len(matrix[0]) < 2):
        return matrix
    
    m = len(matrix[0])
    n = len(matrix)
    queue = []
    
    for j in range(m):
        if matrix[0][j] == 1:
            queue.append((0, j))
            
        if matrix[n - 1][j] == 1:
            queue.append((n - 1, j))
    
    if n > 2:
        for i in range(1, n - 1):
            if matrix[i][0] == 1:
                queue.append((i, 0))
                
            if matrix[i][m - 1]:
                queue.append((i, m - 1))
                
    while len(queue) > 0:
        i, j = queue.pop(-1)
        matrix[i][j] = 2
        
        for point in neighbours(matrix, n, m, i, j):
            queue.append(point)
            
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1
                
    return matrix

def neighbours(matrix, n, m, i, j):
    points = []
    
    if (i > 0) and (matrix[i - 1][j] == 1):
        points.append((i - 1, j))
        
    if (i < n - 1) and (matrix[i + 1][j] == 1):
        points.append((i + 1, j))
        
    if (j > 0) and (matrix[i][j - 1] == 1):
        points.append((i, j - 1))
        
    if (j < m - 1) and (matrix[i][j + 1] == 1):
        points.append((i, j + 1))
    
    return points
