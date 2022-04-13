# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	outputArray = []
	findSuccessorHelper(tree, node, [], outputArray)
	
	if len(outputArray) == 0:
		return
	
	return outputArray[0]
		
def findSuccessorHelper(tree, node, array, outputArray):		
	if (tree.left is not None) and (tree.right is not None):
		findSuccessorHelper(tree.left, node, array, outputArray)
		
		if isMatch(array, node):
			outputArray.append(tree)
			return
		
		array.append(tree.value)		
		findSuccessorHelper(tree.right, node, array, outputArray)
	elif tree.left is not None:
		findSuccessorHelper(tree.left, node, array, outputArray)
		
		if isMatch(array, node):
			outputArray.append(tree)
			return
		
		array.append(tree.value)
	elif tree.right is not None:
		if isMatch(array, node):
			outputArray.append(tree)
			return
		
		array.append(tree.value)		
		findSuccessorHelper(tree.right, node, array, outputArray)
	else:
		if isMatch(array, node):
			outputArray.append(tree)
			return
		
		array.append(tree.value)
		
def isMatch(array, node):
	return (len(array) > 0) and (array[-1] == node.value)
