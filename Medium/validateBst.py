# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return validateHelper(tree, float('-inf'), float('inf'))

def validateHelper(node, minValue, maxValue):
	result = (minValue <= node.value < maxValue)
	leftResult = True
	rightResult = True
	
	if node.left is not None:
		leftResult = validateHelper(node.left, minValue, node.value)
		
	if node.right is not None:
		rightResult = validateHelper(node.right, node.value, maxValue)
		
	return result and leftResult and rightResult
