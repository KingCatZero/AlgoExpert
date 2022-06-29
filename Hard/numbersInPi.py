def numbersInPi(pi, numbers):
    minCuts = [-1] * len(pi)
    numberLookup = set(numbers)
    
    for i in range(len(pi) - 1, -1, -1):        
        if pi[i :] in numberLookup:
            minCuts[i] = 0
        else:
            minCutsForSubstring = float('inf')
            
            for j in range(i + 1, len(pi)):                
                if (pi[i : j] in numberLookup) and (minCuts[j] >= 0):
                    minCutsForSubstring = min(minCutsForSubstring, minCuts[j] + 1)                    
                
            if minCutsForSubstring < float('inf'):
                minCuts[i] = minCutsForSubstring
                
    return minCuts[0]
