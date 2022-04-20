def minimumAreaRectangle(points):
    minArea = 0
    verticalLines = set()
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if canMakeLine(points[i][0], points[i][1], points[j][0], points[j][1]):
                if points[i][1] < points[j][1]:
                    verticalLines.add((points[i][0], points[i][1], points[j][1]))
                else:
                    verticalLines.add((points[i][0], points[j][1], points[i][1]))
                
    for x1, b1, t1 in verticalLines:
        for x2, b2, t2 in verticalLines:
            if canMakeRectangle(x1, b1, t1, x2, b2, t2):
                if minArea == 0:
                    minArea = area(x1, x2, b2, t2)
                else:
                    minArea = min(minArea, area(x1, x2, b2, t2))
    
    return minArea

def canMakeLine(x1, y1, x2, y2):
    return (x1 == x2) and (y1 != y2)

def canMakeRectangle(x1, b1, t1, x2, b2, t2):
    return (x1 != x2) and (b1 == b2) and (t1 == t2)

def area(x1, x2, b, t):
    return abs(x1 - x2) * (t - b)
