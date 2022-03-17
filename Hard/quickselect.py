def quickselect(array, k):
    return quickselectHelper(array, k - 1, 0, len(array) - 1)
    
def quickselectHelper(array, k, l, r):
    while True:        
        if l == r:
            return array[l]
        
        p = quickselectPartition(array, l, r)
        
        if p >= k:
            r = p
        else:
            l = p + 1
    
def quickselectPartition(array, l, r):
    p = (l + r) // 2
    i = l - 1
    j = r + 1
    
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
