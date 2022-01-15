def isMonotonic(array):
    if len(array) < 2:
		return True
	
	sign = 0
	
	for i in range(len(array) - 1):
		if array[i] < array[i + 1]:
			if sign == -1:
				return False
			else:
				sign = 1
		elif array[i] > array[i + 1]:
			if sign == 1:
				return False
			else:
				sign = -1
				
	return True
