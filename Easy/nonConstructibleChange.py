def nonConstructibleChange(coins):
	if len(coins) == 0:
		return 1
	
	coins = sorted(coins)
	
	if coins[0] > 1:
		return 1
	
    coinCombinations = [coins[0]]
	
	for i in range(1, len(coins)):
		if coins[i] > coinCombinations[-1] + 1:
			return coinCombinations[-1] + 1
		else:
			l = len(coinCombinations)
			
			for j in range(l):
				coinCombinations.append(coinCombinations[j] + coins[i])
				
	return coinCombinations[-1] + 1
