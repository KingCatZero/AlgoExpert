def taskAssignment(k, tasks):
    result = []
    l = len(tasks)
    tasks = list(map(lambda i: (tasks[i], i), list(range(l))))
    tasks = sorted(tasks, key = lambda x: x[0])
    
    if l % 2 == 0:
        mid = (l // 2) - 1
    else:
        mid = (l - 1) // 2
    
    for i in range(mid + 1):
        result.append([tasks[i][1], tasks[l - i - 1][1]])
        
    return result
  
