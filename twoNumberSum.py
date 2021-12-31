def twoNumberSum(array, targetSum):
    lookup = set()
    
	for a in array:		
		b = targetSum - a
        
		if b in lookup:
			return [b, a]
		else:
			lookup.add(a)
            
	return []