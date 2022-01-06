def nodeDepths(root):
	totalHeight = 0
    stack = [(root, 0)]
	
	while len(stack) > 0:
		node, height = stack.pop()
		totalHeight += height
		
		if node.left is not None:
			stack.append((node.left, height + 1))
			
		if node.right is not None:
			stack.append((node.right, height + 1))
			
	return totalHeight


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
