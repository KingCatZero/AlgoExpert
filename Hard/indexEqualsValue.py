def indexEqualsValue(array):
    if len(array) == 0:
        return -1
    
    l = 0
    r = len(array) - 1
    j = -1
    
    while l < r:
        i = (l + r) // 2
        
        if i == array[i]:
            j = i
            r = i - 1
        elif i < array[i]:
            r = i - 1
        else:
            l = i + 1
    
    if l == array[l]:
        return l
    
    return j
