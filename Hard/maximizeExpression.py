def maximizeExpression(array):
    n = 4
    
    if len(array) < n:
        return 0
    
    maxTerms = [([float('-inf')] * (len(array) + 1)) for i in range(n)]
    maxTerms.insert(0, [0] * (len(array) + 1))
    signs = [1, -1, 1, -1]
    
    for i in range(1, n + 1):
        for j in range(i, len(array) + i - n + 1):
            maxTerms[i][j] = max(maxTerms[i][j - 1], maxTerms[i - 1][j - 1] + (array[j - 1] * signs[i - 1]))
        
    return maxTerms[-1][-1]
