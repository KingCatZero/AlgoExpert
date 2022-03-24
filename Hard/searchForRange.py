def searchForRange(array, target):
    i = binarySearch(array, target)
    
    if i == -1:
        return [-1, -1]
    
    l = linearRangeSearch(array, target, i, 'left')
    r = linearRangeSearch(array, target, i, 'right')
    return [l, r]

def linearRangeSearch(array, target, startIndex, direction):
    if direction == 'left':
        for i in range(startIndex, -1, -1):
            if array[i] != target:
                return i + 1
            
        return 0
    else:
        for i in range(startIndex, len(array)):
            if array[i] != target:
                if array[i] != target:
                    return i - 1
            
        return len(array) - 1

def binarySearch(array, target):
    l = 0
    r = len(array) - 1
    
    while l <= r:
        i = (l + r) // 2
        
        if array[i] == target:
            return i
        elif array[i] < target:
            l = i + 1
        else:
            r = i - 1
            
    return -1
