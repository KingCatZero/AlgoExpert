from math import ceil

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class GlobalIndex():
    def __init__(self, n):
        self.n = n

def reconstructBst(preOrderTraversalValues):
    globalIndex = GlobalIndex(0)
    return reconstructBstHelper(preOrderTraversalValues, float('-inf'), float('inf'), globalIndex)

def reconstructBstHelper(array, lowerBound, upperBound, globalIndex):
    if globalIndex.n == len(array):
        return None
    
    value = array[globalIndex.n]
    
    if (value < lowerBound) or (value >= upperBound):
        return None
    
    globalIndex.n += 1
    leftSubtree = reconstructBstHelper(array, lowerBound, value, globalIndex)
    rightSubtree = reconstructBstHelper(array, value, upperBound, globalIndex)
    return BST(value, leftSubtree, rightSubtree)
