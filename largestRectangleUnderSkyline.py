def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    stack = []
    
    for i in range(len(buildings)):        
        while (len(stack) > 0) and (buildings[stack[-1]] > buildings[i]):
            valueToRemove = buildings[stack[-1]]
            
            while (len(stack) > 0) and (buildings[stack[-1]] == valueToRemove):
                stack.pop()
                
            if len(stack) == 0:
                maxArea = max(maxArea, valueToRemove * i)
            else:
                maxArea = max(maxArea, valueToRemove * (i - stack[-1] - 1))
                valueToRemove = buildings[stack[-1]]
        
        stack.append(i)
        
    if len(stack) > 0:
        buildings[0] = buildings[stack[0]]
        stack[0] = 0
        
    for i in range(len(stack)):
        maxArea = max(maxArea, buildings[stack[i]] * (len(buildings) - stack[i]))
            
    return maxArea
