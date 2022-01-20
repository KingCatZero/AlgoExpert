def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
      return 0
    elif len(array) == 1:
      return array[0]
    elif len(array) == 2:
      return max(array)
	
	maxSums = [array[0], array[1], array[0] + array[2]]
	
	for i in range(3, len(array)):
		new = max(maxSums[0], maxSums[1]) + array[i]
		maxSums[0] = maxSums[1]
		maxSums[1] = maxSums[2]
		maxSums[2] = new
		
	return max(maxSums[1], maxSums[2])
