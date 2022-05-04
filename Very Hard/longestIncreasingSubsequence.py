def longestIncreasingSubsequence(array):
    subsequenceIndexes = [-1] * len(array)
    subsequenceEnds = [-1] * len(array)
    longestLength = 0
    
    for i in range(len(array)):
        j = binarySearch(array, subsequenceEnds, longestLength, array[i])
        longestLength = max(longestLength, j + 1)
        
        if subsequenceEnds[j] == -1:
            subsequenceEnds[j] = i
        elif array[i] < array[subsequenceEnds[j]]:
            subsequenceEnds[j] = i
            
        if j == 0:
            subsequenceIndexes[i] = -1
        else:
            subsequenceIndexes[i] = subsequenceEnds[j - 1]
			
    return maxSubsequence(array, subsequenceIndexes, subsequenceEnds[: longestLength][-1])

def maxSubsequence(array, subsequenceIndexes, index):
    output = []
    
    while index >= 0:
        output.append(array[index])
        index = subsequenceIndexes[index]
    
    return output[:: -1]

def binarySearch(array, arrayIndexes, arrayIndexesLength, x):
    l = 0
    r = arrayIndexesLength - 1
    
    if r == -1:
        return 0
    elif array[arrayIndexes[r]] < x:
        return r + 1
	
	while l < r:
        m = (l + r) // 2
		
        if array[arrayIndexes[m]] < x <= array[arrayIndexes[m + 1]]:
            return m + 1
        elif array[arrayIndexes[m]] < x:
            l = m
        else:
            r = m
    
    return l
