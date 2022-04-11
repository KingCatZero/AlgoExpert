def apartmentHunting(blocks, reqs):
    numberOfBlocks = len(blocks)	
	allReqDistances = distances(blocks, reqs, numberOfBlocks)    
    return minOverallDistanceIndex(allReqDistances, reqs, numberOfBlocks)

def minOverallDistanceIndex(allArrays, reqs, numberOfBlocks):
    index = 0
    minDistance = numberOfBlocks
    
    for i in range(numberOfBlocks):
        leftOrRightDistance = 0
        
        for j in range(len(reqs)):
            leftOrRightDistance = max(leftOrRightDistance, abs(i - allArrays[j][i]))
        
        if leftOrRightDistance < minDistance:
            minDistance = leftOrRightDistance
            index = i
            
    return index

def distances(blocks, reqs, numberOfBlocks):
	allArrays = []
    
    for i in range(len(reqs)):
        array = [-1] * numberOfBlocks
        array = distancesFromRange(array, blocks, reqs[i], range(numberOfBlocks))
        array = distancesFromRange(array, blocks, reqs[i], range(numberOfBlocks - 1, -1, -1))
        allArrays.append(array)
		
	return allArrays
    
def distancesFromRange(array, blocks, req, indexRange):
    j = -1

    for i in indexRange:
        if blocks[i][req]:
            j = i
            
        if j >= 0:
            if array[i] == -1:
                array[i] = j
            elif abs(i - j) < abs(i - array[i]):
                array[i] = j
            
    return array
