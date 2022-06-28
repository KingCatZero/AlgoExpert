def palindromePartitioningMinCuts(string):
    if len(string) < 2:
        return 0
        
    palMatrix = palindromicityMatrix(string)
    minCuts = [0] * len(string)
    
    for j in range(1, len(string)):
        minCutsForSubstring = float('inf')
        
        for i in range(j):
            if palMatrix[i][j] == 1:
                if i == 0:
                    minCutsForSubstring = 0
                else:
                    minCutsForSubstring = min(minCutsForSubstring, minCuts[i - 1] + 1)
                
        minCuts[j] = min(minCutsForSubstring, minCuts[j - 1] + 1)
    
    return minCuts[-1]

def palindromicityMatrix(string):
    output = [([0] * len(string)) for i in range(len(string))]
    
    for i in range(len(string)):
        output[i][i] = 1
        
    for j in range(1, len(string)):
        for i in range(j):
            if string[i] == string[j]:
                if string[i] == string[j]:
                    if (i == j - 1) or (output[i + 1][j - 1] == 1):
                        output[i][j] = 1
    
    return output
