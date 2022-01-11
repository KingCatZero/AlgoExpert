def productSum(array):
    return productSumHelper(array, 1)

def productSumHelper(array, depth):
    total = 0
    
    for a in array:
        if isinstance(a, list):
            total = total + (productSumHelper(a, depth + 1))
        else:
            total += a
            
    return total * depth
