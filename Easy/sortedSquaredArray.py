def sortedSquaredArray(array):
    squares = [0] * len(array)
	l = 0
	r = len(array) - 1
	i = len(array) - 1
	
	while l <= r:
		if abs(array[l]) <= abs(array[r]):
			squares[i] = array[r] ** 2
			r -= 1
		else:
			squares[i] = array[l] ** 2
			l += 1
			
		i -= 1
	
	return squares
