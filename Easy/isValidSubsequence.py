def isValidSubsequence(array, sequence):
    i = 0
	
	for a in array:
		if a == sequence[i]:
			i += 1
			
			if i == len(sequence):
				return True
			
	return False
