def waterArea(heights):
	if len(heights) == 0:
		return 0
	
    area = 0
    leftWalls = [0] * len(heights)
    leftWall = heights[0]
    rightWall = heights[-1]
    
    for i in range(len(heights)):
        leftWall = max(leftWall, heights[i])
        leftWalls[i] = leftWall
        
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] < rightWall:
            if leftWalls[i] < rightWall:
                area = area + leftWalls[i] - heights[i]
            else:
                area = area + rightWall - heights[i]
        else:
            rightWall = heights[i]
            
    return area
