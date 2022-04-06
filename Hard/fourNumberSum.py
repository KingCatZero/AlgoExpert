def fourNumberSum(array, targetSum):
    solutions = []
    fourNumberSumHelper(array, targetSum, 0, [], solutions)
    return solutions

def fourNumberSumHelper(array, targetSum, i, subarray, solutions):
    if (i == len(array)) or (len(subarray) == 4):
        if (targetSum == 0) and (len(subarray) == 4):
            solutions.append(subarray)
        
        return
            
    fourNumberSumHelper(array, targetSum, i + 1, subarray, solutions)
    fourNumberSumHelper(array, targetSum - array[i], i + 1, subarrayWithValue(subarray, array[i]), solutions)
    
def subarrayWithValue(subarray, value):
    newSubarray = subarray[:]
    newSubarray.append(value)
    return newSubarray
