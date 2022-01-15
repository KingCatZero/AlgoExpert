def moveElementToEnd(array, toMove):
    l = 0
	r = len(array) - 1
	
	while l < r:
		if array[l] != toMove:
			l += 1
		elif array[r] == toMove:
			r -= 1
		else:
			array[l], array[r] = array[r], array[l]
		
	return array
