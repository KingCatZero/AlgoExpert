def minimumPassesOfMatrix(matrix):
    passCount = 0
    negativeCount = 0
    queue = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                queue.append((i, j))
            elif matrix[i][j] < 0:
                negativeCount += 1
                
    if negativeCount == 0:
        return 0
                
    while True:
        passCount += 1
        nextQueue = []
        
        for iCurrent, jCurrent in queue:
            for i, j in negativeNeighbours(matrix, iCurrent, jCurrent):
                matrix[i][j] *= -1
                nextQueue.append((i, j))
                negativeCount -= 1
        
        if len(nextQueue) == 0:
            if negativeCount > 0:
                return -1
            else:
                break
        else:
            if negativeCount > 0:
                queue = nextQueue[:]
            else:
                break
    
    return passCount

def negativeNeighbours(matrix, i, j):
    neighbours = []
    
    if (i > 0) and (matrix[i - 1][j] < 0):
        neighbours.append((i - 1, j))
        
    if (i < len(matrix) - 1) and (matrix[i + 1][j] < 0):
        neighbours.append((i + 1, j))
        
    if (j > 0) and (matrix[i][j - 1] < 0):
        neighbours.append((i, j - 1))
        
    if (j < len(matrix[0]) - 1) and (matrix[i][j + 1] < 0):
        neighbours.append((i, j + 1))
            
    return neighbours
