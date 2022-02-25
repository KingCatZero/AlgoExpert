def hasSingleCycle(array):
    visitCount = 0
    l = len(array)
    i = 0
    
    while visitCount < l:
        if array[i] == 0:
            return False
        else:
            visitCount += 1
            i = (i + array[i]) % l
            
            if (i == 0) and (visitCount < l):
                return False
            
    return i == 0
