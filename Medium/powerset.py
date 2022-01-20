def powerset(array):
    l = len(array)
    store = []
    queue = [([], 0)]
    
    while len(queue) > 0:
        currentSet, i = queue.pop(0)
        store.append(currentSet)
        
        for j in range(i, l):
            newSet = list(currentSet) + [array[j]]
            queue.append((newSet, j + 1))
            
    return store
