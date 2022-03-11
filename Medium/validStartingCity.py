def validStartingCity(distances, fuel, mpg):
    index = 0
	maxNegativeDiff = 0
	runningDiff = 0

	for i in range(len(distances)):		
		if runningDiff < maxNegativeDiff:
			maxNegativeDiff = runningDiff
			index = i
			
		runningDiff = runningDiff + (fuel[i] * mpg) - distances[i]
			
	return index
