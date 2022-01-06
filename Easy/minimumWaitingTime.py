def minimumWaitingTime(queries):
	totalWaitTime = 0
	waitTime = 0
	
	for query in sorted(queries)[: -1]:
		waitTime += query
		totalWaitTime += waitTime
		
	return totalWaitTime
