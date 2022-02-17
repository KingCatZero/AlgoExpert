def quickSort(array):
    return quickSortHelper(array, 0, len(array) - 1)

def quickSortHelper(array, l, r):
    if l < r:
        p = quickSortPartition(array, l, r)
        quickSortHelper(array, l, p)
        quickSortHelper(array, p + 1, r)
    
    return array

def quickSortPartition(array, l, r):
    i = l - 1
    j = r + 1
    
    if (r - l) % 2 == 0:
        p = (l + r) // 2
    else:
        p = (l + r - 1) // 2
        
    while True:
        while True:
            i += 1
            
            if array[i] >= array[p]:
                break
                
        while True:
            j -= 1
            
            if array[j] <= array[p]:
                break
                
        if i < j:
            swap(array, i, j)
            
            if i == p:
                p = j
            elif j == p:
                p = i
            
        else:
            return j
        
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
