def shiftedBinarySearch(array, target):
    l = 0
    r = len(array) - 1
    
    while l <= r:
        i = (l + r) // 2
        
        if array[i] == target:
            return i
        elif array[i] < target:
            if inRightSubarray(array, target, r, i):
                l = i + 1
            else:
                r = i - 1
        else:
            if inLeftSubarray(array, target, l, i):
                r = i - 1
            else:
                l = i + 1
    
    return -1

def inRightSubarray(array, target, r, i):
    return (array[r] >= target) or (array[r] < array[i])

def inLeftSubarray(array, target, l, i):
    return (array[l] <= target) or (array[l] > array[i])
