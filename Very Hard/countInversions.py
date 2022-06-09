class Inversions():
    def __init__(self):
        self.count = 0
        
inversions = Inversions()

def countInversions(array):
    inversions.count = 0
    mergeSortHelper(array, 0, len(array) - 1)
    return inversions.count

def mergeSortHelper(array, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSortHelper(array, l, m)
        mergeSortHelper(array, m + 1, r)
        mergePartitions(array, array[l : m + 1], array[m + 1 : r + 1], l)

def mergePartitions(array, left, right, partitionStartIndex):
    i = 0
    j = 0
    k = partitionStartIndex
    
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1
            inversions.count = inversions.count + len(left) - i
    
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
