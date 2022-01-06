# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	totals = []
    stack = [(root, root.value)]
	
	while len(stack) > 0:
		node, total = stack.pop()
		
		if (node.left is None) and (node.right is None):
			totals.append(total)
		else:		
			if node.right is not None:
				stack.append((node.right, node.right.value + total))

			if node.left is not None:
				stack.append((node.left, node.left.value + total))
				
	return totals
