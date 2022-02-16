def minNumberOfCoinsForChange(n, denoms):
    minCoins = [0] + ([-1] * n)
    
    for d in denoms:
        for i in range(d, n + 1):                
            if i == d:
                minCoins[i] = 1
            elif minCoins[i - d] != -1:
                if minCoins[i] == -1:
                    minCoins[i] = minCoins[i - d] + 1
                else:
                    minCoins[i] = min(minCoins[i], minCoins[i - d] + 1)
        
    return minCoins[-1]
