def staircaseTraversal(height, maxSteps):    
    stairs = ([1] * maxSteps) + ([0] * (height - maxSteps))
    
    for i in range(1, height):
        s = min(i, maxSteps) + 1
        
        for j in range(1, s):
            stairs[i] += stairs[i - j]
        
    return stairs[-1]
