def findClosestValueInBst(tree, target):
	closestValue = tree.value
	queue = [tree]
	
	while len(queue) > 0:
		node = queue.pop(0)
		
		if node.value == target:
			return target
		elif abs(target - node.value) < abs(target - closestValue):
			closestValue = node.value
			
		if node.left is not None:
			if node.value > target:
				queue.append(node.left)
		
		if node.right is not None:
			if node.value < target:
				queue.append(node.right)
				
	return closestValue

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
