# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
	diameters = []
    binaryTreeDiameterHelper(tree, diameters)
	return max(diameters)

def binaryTreeDiameterHelper(node, array):
	if node.left is None:
		leftDiameter = 0
	else:
		leftDiameter = max(binaryTreeDiameterHelper(node.left, array)) + 1
		
	if node.right is None:
		rightDiameter = 0
	else:
		rightDiameter = max(binaryTreeDiameterHelper(node.right, array)) + 1
		
	array.append(leftDiameter + rightDiameter)
	return (leftDiameter, rightDiameter)
