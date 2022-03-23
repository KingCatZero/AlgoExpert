def minNumberOfJumps(array):
	if len(array) < 2:
		return 0
	
    count = 0
    i = 0
    
    while i < len(array):
        count += 1
        
        if i + array[i] >= len(array) - 1:
            break
        
        biggestJump = 0
        biggestJumpIndex = i + 1
        
        for j in range(i + 1, i + array[i] + 1):
            if j + array[j] > biggestJump:
                biggestJump = j + array[j]
                biggestJumpIndex = j
                
        i = biggestJumpIndex
    
    return count
