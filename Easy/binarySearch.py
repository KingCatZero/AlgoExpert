def binarySearch(array, target):
	l = 0
    r = len(array) - 1
    
    while l < r:        
        if (r - l) % 2 == 0:
            m = (r + l) // 2
        else:
            m = (r + l - 1) // 2
            
        if array[m] == target:
            return m
        elif array[m] < target:
            l = m + 1
        else:
            r = m
            
    if array[l] == target:
        return l
    
    return -1
