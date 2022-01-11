def firstNonRepeatingCharacter(string):
	j = len(string)
    lookup = {}
	
	for i in range(len(string)):
		if string[i] in lookup:
			lookup[string[i]][0] = False
		else:
			lookup[string[i]] = [True, i]
		
	for isSingle, i in lookup.values():
		if isSingle and (i < j):
			j = i
			
	if j == len(string):
		return -1
	
	return j
