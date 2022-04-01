def maxSumIncreasingSubsequence(array):
    previousIndexes = [-1] * len(array)
    runningTotals = array[:]
    k = 0
    count = 0
    
    for i in range(len(array)):
        for j in range(i):
            if (array[j] < array[i]) and (runningTotals[j] + array[i] >= runningTotals[i]):
                previousIndexes[i] = j
                runningTotals[i] = runningTotals[j] + array[i]
            
        if runningTotals[i] > runningTotals[k]:
            k = i
            
    return [runningTotals[k], subsequence(array, previousIndexes, k)]
    
def subsequence(array, previousIndexes, i):
    newArray = []
    
    while i >= 0:
        newArray.append(array[i])
        i = previousIndexes[i]
    
    return newArray[:: -1]
