def longestCommonSubsequence(str1, str2):
	if (len(str1) == 0) or (len(str2) == 0):
		return []
	
    matrix = createMatrix(str1, str2)
    longestSubsequenceLengths = [0] * len(str1)
    longestSubsequenceRows = [1] * len(str1)
    
    for i in range(2, len(matrix)):
        k = longestSubsequenceIndex(str1, matrix[i][0], longestSubsequenceLengths)
        l = nextCharIndex(str1, matrix[i][0], k)
        
        if l == 0:
            matrix[i][2] = matrix[i][0]
            longestSubsequenceLengths[l] = 1
            longestSubsequenceRows[l] = i
        elif l > 0:
            for j in range(2, k + 3):
                row = longestSubsequenceRows[k]
                matrix[i][j] = matrix[row][j]
                
            matrix[i][l + 2] = matrix[i][0]
            longestSubsequenceLengths[l] = longestSubsequenceLengths[k] + 1
            longestSubsequenceRows[l] = i
    
    return longestSubsequence(matrix, longestSubsequenceLengths, longestSubsequenceRows)
    
def longestSubsequenceIndex(string, c, longestSubsequenceLengths):
    index = -1
    storedIndex = -1
    
    for j in range(len(string)):
        if (index == -1) or (longestSubsequenceLengths[j] > longestSubsequenceLengths[index]):
            index = j
            
        if string[j] == c:
            if (storedIndex == -1) or (longestSubsequenceLengths[index] > longestSubsequenceLengths[storedIndex]):
                storedIndex = index
                
    return storedIndex

def nextCharIndex(string, c, k):
    if (k == 0) and (c == string[0]):
        return k
    
    for j in range(k + 1, len(string)):
        if string[j] == c:
            return j
        
    return -1

def longestSubsequence(matrix, longestSubsequenceLengths, longestSubsequenceRows):
    index = -1
    
    for j in range(len(longestSubsequenceLengths)):
        if (index == -1) or (longestSubsequenceLengths[j] > longestSubsequenceLengths[index]):
            index = j
            
    row = longestSubsequenceRows[index]
    subsequence = []
            
    for j in range(2, len(matrix[0])):
        if matrix[row][j] != '-':
            subsequence.append(matrix[row][j])
            
    return subsequence

def createMatrix(str1, str2):
    emptyChar = '-'
    matrix = []
    matrix.append([emptyChar, emptyChar] + list(str1))
    matrix.append([emptyChar] * (len(str1) + 2))
    
    for i in range(len(str2)):
        matrix.append([str2[i]] + ([emptyChar] * (len(str1) + 1)))
    
    return matrix
