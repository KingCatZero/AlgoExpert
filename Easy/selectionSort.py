def selectionSort(array):
    for i in range(len(array) - 1):
		s = i
		
		for j in range(i, len(array)):
			if array[j] < array[s]:
				s = j
				
		array[i], array[s] = array[s], array[i]
		
	return array
