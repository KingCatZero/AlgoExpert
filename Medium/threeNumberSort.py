def threeNumberSort(array, order):
    counts = {}
    
    for a in array:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1
            
    start = 0
            
    for i in range(3):
        if order[i] in counts:
            count = counts[order[i]]

            for j in range(start, start + count):
                array[j] = order[i]

            start += count
    
    return array
  
