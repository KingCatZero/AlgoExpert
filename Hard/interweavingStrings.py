def interweavingStrings(one, two, three):
    queue = [(0, 0, 0)]
    cache = set()
    
    while len(queue) > 0:
        i, j, k = queue.pop(0)
        
        if k == len(three):
            return (i == len(one)) and (j == len(two))
        
        if (i < len(one)) and (one[i] == three[k]) and ((i + 1, j) not in cache):
            queue.append((i + 1, j, k + 1))
            cache.add((i + 1, j))
            
        if (j < len(two)) and (two[j] == three[k]) and ((i, j + 1) not in cache):
            queue.append((i, j + 1, k + 1))
            cache.add((i, j + 1))
    
    return False
