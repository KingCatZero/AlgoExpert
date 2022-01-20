def arrayOfProducts(array):
	n = len(array)
	result = [1] * n
    fromLeft = [array[0]] * n
	fromRight = [array[-1]] * n
	
	for l in range(1, n):
		r = n - l - 1
		fromLeft[l] = fromLeft[l - 1] * array[l]
		fromRight[r] = fromRight[r + 1] * array[r]
		
	for i in range(n):
		if i == 0:
			result[i] = fromRight[i + 1]
		elif i == n - 1:
			result[i] = fromLeft[i - 1]
		else:
			result[i] = fromLeft[i - 1] * fromRight[i + 1]
		
	return result
