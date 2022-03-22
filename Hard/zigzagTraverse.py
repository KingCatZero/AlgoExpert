def zigzagTraverse(array):
    output = []
    height = len(array)
    width = len(array[0])
    shortSide = min(height, width)
    longSide = max(height, width)
    
    for z in range(height + width - 1):
        if z % 2 == 0:
            directions = [1, -1]
            
            if z < width:
                row, col = 0, z
            else:
                row, col = z - width + 1, width - 1
        else:
            directions = [-1, 1]
            
            if z < height:
                row, col = z, 0
            else:
                row, col = height - 1, z - height + 1
                
        
        if z < shortSide - 1:
            stepCount = z + 1
        elif z < longSide:
            stepCount = shortSide
        else:
            stepCount = shortSide + longSide - z - 1
        
        for step in range(stepCount):
            output.append(array[row][col])
            row += directions[0]
            col += directions[1]
    
    return output
