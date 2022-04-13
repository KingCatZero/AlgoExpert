def lineThroughPoints(points):
    if len(points) < 2:
        return len(points)
    
    maxLineCount = 0
    slopes = {}
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            s = slope(points[i][0], points[i][1], points[j][0], points[j][1])
            p1 = (points[i][0], points[i][1])
            p2 = (points[j][0], points[j][1])
            
            if s not in slopes:
                slopes[s] = {}
                
            commonPoints = slopes[s]
            
            if p1 not in commonPoints:
                commonPoints[p1] = []
                
            commonPoints[p1].append(p2)
            
            if p2 not in commonPoints:
                commonPoints[p2] = []
                
            commonPoints[p2].append(p1)
            
    for s in slopes:
        for p in slopes[s]:
            maxLineCount = max(maxLineCount, len(slopes[s][p]) + 1)
    
    return maxLineCount
            
def slope(x1, y1, x2, y2):
    if x1 == x2:
        return float('inf')
    
    return (y2 - y1) / (x2 - x1)
