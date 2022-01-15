def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
	arrayTwo = sorted(arrayTwo)
	iOne = 0
	iTwo = 0
	result = [arrayOne[0], arrayTwo[0]]
	smallestDiff = abs(arrayOne[0] - arrayTwo[0])
	
	while (iOne < len(arrayOne)) and (iTwo < len(arrayTwo)) and (smallestDiff != 0):
		if abs(arrayOne[iOne] - arrayTwo[iTwo]) < smallestDiff:
			result = [arrayOne[iOne], arrayTwo[iTwo]]
			smallestDiff = abs(arrayOne[iOne] - arrayTwo[iTwo])
			
		if smallestDiff == 0:
			return result
		elif arrayOne[iOne] < arrayTwo[iTwo]:
			iOne += 1
		else:
			iTwo += 1
	
	return result
