def threeNumberSum(array, targetSum):
    arrays = []
    array = sorted(array)
    
    for i in range(len(array) - 2):
        l = i + 1
        r = len(array) - 1
        
        while l < r:
            currentSum = array[i] + array[l] + array[r]

            if currentSum == targetSum:
                arrays.append((array[i], array[l], array[r]))
                l += 1
                r -= 1
            elif currentSum < targetSum:
                l += 1
            else:
                r -= 1
    
    return arrays
