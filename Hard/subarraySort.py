def subarraySort(array):
    minValue = array[-1]
    minUnordered = array[-1]
    maxValue = array[0]
    maxUnordered = array[0]
    
    for l in range(len(array)):
        r = len(array) - l - 1
        
        if array[r] <= minValue:
            minValue = array[r]
        else:
            minUnordered = minValue
            
        if array[l] >= maxValue:
            maxValue = array[l]
        else:
            maxUnordered = maxValue
            
    if minUnordered > maxUnordered:
        return [-1, -1]
            
    l = 0
    r = len(array) - 1
    
    for l in range(len(array)):
        if array[l] > minUnordered:
            break
            
    for r in range(len(array) - 1, -1, -1):
        if array[r] < maxUnordered:
            break
            
    return [l, r]
