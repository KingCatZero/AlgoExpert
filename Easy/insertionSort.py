def insertionSort(array):
    new = [0] * len(array)
	i = -1
	
	while len(array) > 0:
		a = array.pop()
		i += 1
		new[i] = a
		
		for j in range(i, 0, -1):
			if new[j] < new[j - 1]:
				new[j], new[j - 1] = new[j - 1], new[j]
			else:
				break
	
	return new
