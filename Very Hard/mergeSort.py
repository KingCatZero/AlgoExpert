def mergeSort(array):
    mergeSortHelper(array, 0, len(array) - 1)
    return array

def mergeSortHelper(array, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSortHelper(array, l, m)
        mergeSortHelper(array, m + 1, r)
        mergeLeftAndRight(array, array[l : m + 1], array[m + 1 : r + 1], l)

def mergeLeftAndRight(array, left, right, k):
    i = 0
    j = 0
    
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
