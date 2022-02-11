def numberOfWaysToMakeChange(n, denoms):
    numberOfWays = [1] + ([0] * n)
	
	for d in denoms:
		for i in range(d, n + 1):
			numberOfWays[i] += numberOfWays[i - d]
			
	return numberOfWays[-1]
