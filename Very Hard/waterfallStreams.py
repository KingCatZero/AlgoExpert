def waterfallStreams(array, source):
    percentages = [0] * len(array[0])
    percentages[source] = 100.0

    for i in range(len(array) - 1):        
        for j in landingColumns(array, source, i):
            array[i][j] = 2
            
            if array[i + 1][j] == 1:
				leftIndexRange = range(j - 1, -1, -1)
				rightIndexRange = range(j + 1, len(array[0]))
				leftFree = isLeftSpaceFree(array, i, j)
				rightFree = isRightSpaceFree(array, i, j)
			
                if leftFree and rightFree:
                    l = moveLeftOrRight(array, i, leftIndexRange)
                    r = moveLeftOrRight(array, i, rightIndexRange)
					updatePercentages(percentages, array, i, j, l)
					updatePercentages(percentages, array, i, j, r)
						
                elif leftFree:
                    l = moveLeftOrRight(array, i, leftIndexRange)
					updatePercentages(percentages, array, i, j, l)
						
                elif rightFree:
                    r = moveLeftOrRight(array, i, rightIndexRange)
					updatePercentages(percentages, array, i, j, r)

                percentages[j] = 0
    
    return percentages

def updatePercentages(percentages, array, i, j, k):
	if (k >= 0) and (array[i + 1][k] == 0):
		percentages[k] += (percentages[j] / 2)

def landingColumns(array, source, i):
    if i == 0:
        return [source]
    
    output = []
    
    for j in range(len(array[0])):
        if (array[i][j] == 0) and (array[i - 1][j] == 2):
            output.append(j)
    
    return output

def moveLeftOrRight(array, i, indexRange):
    for k in indexRange:
        if array[i][k] != 1:
            array[i][k] = 2
        else:
            break

        if array[i + 1][k] != 1:
            return k

    return -1

def isLeftSpaceFree(array, i, j):
    return (j > 0) and (array[i][j - 1] != 1)

def isRightSpaceFree(array, i, j):
    return (j < len(array[0]) - 1) and (array[i][j + 1] != 1)
