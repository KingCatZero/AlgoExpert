def levenshteinDistance(str1, str2):
	if (len(str1) == 0) or (len(str2) == 0):
		return abs(len(str1) - len(str2))
	
    insertionDistances = list(range(len(str1) + 1))
    
    for i in range(1, len(str2) + 1):
        currentDistances = [i] + ([0] * len(str1))
        
        for j in range(1, len(str1) + 1):
            insDst = insertionDistances[j] + 1
            delDst = currentDistances[j - 1] + 1
            subDst = insertionDistances[j - 1]
            
            if str1[j - 1] != str2[i - 1]:
                subDst += 1
                
            currentDistances[j] = min(insDst, delDst, subDst)
            
        insertionDistances = currentDistances[:]
            
    return currentDistances[-1]
