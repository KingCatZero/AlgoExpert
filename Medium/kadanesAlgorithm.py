def kadanesAlgorithm(array):
	if len(array) == 0:
		return 0
	
    maxSum = array[0]
	currentSum = array[0]
	
	for i in range(1, len(array)):
		currentSum = max(currentSum + array[i], array[i])		
		maxSum = max(maxSum, currentSum)
		
	return maxSum
