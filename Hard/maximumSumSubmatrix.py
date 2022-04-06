def maximumSumSubmatrix(matrix, size):
    partialSums = partialSumMatrix(matrix)
    
    if size == len(partialSums):
        return partialSums[-1][-1]
    
    maxSubmatrixSum = partialSums[size - 1][size - 1]
    
    for i in range(size - 1, len(partialSums)):
        for j in range(size - 1, len(partialSums[0])):
            maxSubmatrixSum = max(maxSubmatrixSum, submatrixSum(partialSums, i, j, size))
            
    return maxSubmatrixSum
    
def partialSumMatrix(matrix):
    partialSums = copyMatrix(matrix)
    
    for j in range(1, len(partialSums[0])):
        partialSums[0][j] = partialSum(partialSums, 0, j)
        
    for i in range(1, len(matrix)):
        partialSums[i][0] = partialSum(partialSums, i, 0)
        
    for i in range(1, len(partialSums)):
        for j in range(1, len(partialSums[0])):
            partialSums[i][j] = partialSum(partialSums, i, j)
        
    return partialSums

def copyMatrix(matrix):
    return [row[:] for row in matrix]

def partialSum(matrix, i, j):
    if (i == 0) and (j == 0):
        return matrix[0][0]
    elif i == 0:
        return matrix[0][j] + matrix[0][j - 1]
    elif j == 0:
        return matrix[i][0] + matrix[i - 1][0]
    
    return matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]

def submatrixSum(matrix, i, j, size):
    if (i < size) and (j < size):
        return matrix[i][j]
    elif i < size:
        return matrix[i][j] - matrix[i][j - size]
    elif j < size:
        return matrix[i][j] - matrix[i - size][j]
    
    return matrix[i][j] - matrix[i - size][j] - matrix[i][j - size] + matrix[i - size][j - size]
