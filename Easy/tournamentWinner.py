def tournamentWinner(competitions, results):
    resultsLookup = {}
	bestResult = ['', -1]
	
	for i in range(len(competitions)):
		if results[i] == 0:
			h = 0
			a = 3
		else:
			h = 3
			a = 0
			
		if competitions[i][0] in resultsLookup:
			resultsLookup[competitions[i][0]] += h
		else:
			resultsLookup[competitions[i][0]] = h
			
		if competitions[i][1] in resultsLookup:
			resultsLookup[competitions[i][1]] += a
		else:
			resultsLookup[competitions[i][1]] = a
			
	for item in resultsLookup.items():
		if item[1] > bestResult[1]:
			bestResult = [item[0], item[1]]
			
	return bestResult[0]
