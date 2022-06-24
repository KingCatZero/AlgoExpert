def topologicalSort(jobs, deps):
    output = []
    X, Y = buildDependencyGraphs(jobs, deps)
    freeJobs = startingJobs(Y)
    print(X)
    print(Y)
    print(freeJobs)
    
    while len(freeJobs) > 0:
        x = freeJobs.pop(0)
        output.append(x)
        
        for y in X[x]:
            Y[y].remove(x)
            
            if len(Y[y]) == 0:
                freeJobs.append(y)
    
    if len(output) < len(jobs):
        return []
    
    return output
    

def buildDependencyGraphs(jobs, deps):
    X = {}
    Y = {}
    
    for job in jobs:
        X[job] = set()
        Y[job] = set()
        
    for dep in deps:
        X[dep[0]].add(dep[1])
        Y[dep[1]].add(dep[0])
        
    return X, Y

def startingJobs(Y):
    return list(filter(lambda job: len(Y[job]) == 0, Y))
