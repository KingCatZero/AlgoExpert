def firstDuplicateValue(array):	
	for a in array:
		i = abs(a) - 1
		
		if array[i] < 0:
			return abs(a)
		else:
			array[i] *= -1
				
	return -1
