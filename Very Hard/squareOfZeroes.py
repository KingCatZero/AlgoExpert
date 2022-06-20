def squareOfZeroes(matrix):
    counts = buildCounterMatrix(matrix)
    
    for i in range(len(counts)):
        for j in range(len(counts)):
            if hasSquare(counts, i, j):
                return True
            
    return False

def hasSquare(counts, i, j):
    x = min(counts[i][j][0], counts[i][j][1])
    return (x > 0) and (counts[i + x][j][1] == x) and (counts[i][j + x][0] == x)
            
def buildCounterMatrix(matrix):
    counts = [row[:] for row in matrix]
        
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix) - 1, -1, -1):
            counts[i][j] = [0, 0]
            
            if matrix[i][j] == 0:
                counts[i][j][0] = zerosBelow(counts, matrix, i, j)
                counts[i][j][1] = zerosRight(counts, matrix, i, j)
    
    return counts

def zerosBelow(counts, matrix, i, j):
    if (i == len(matrix) - 1) or (matrix[i + 1][j] == 1):
        return 0
    
    return counts[i + 1][j][0] + 1
    
def zerosRight(counts, matrix, i, j):
    if (j == len(matrix) - 1) or (matrix[i][j + 1] == 1):
        return 0
    
    return counts[i][j + 1][1] + 1
