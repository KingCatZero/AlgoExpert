# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
		
		while True:
			if node.value > value:
				if node.left is None:
					node.left = BST(value)
					return
				else:
					node = node.left
			else:
				if node.right is None:
					node.right = BST(value)
					return
				else:
					node = node.right

    def contains(self, value):
        node = self
		
		while node is not None:
			if node.value == value:
				return True
			elif node.value > value:
				node = node.left
			else:
				node = node.right
				
		return False

    def remove(self, value, parentNode = None):
		node = self
		
		while True:
			if node is None:
				return
			elif node.value == value:
				break
			elif node.value > value:
				parentNode = node
				node = node.left
			else:
				parentNode = node
				node = node.right
				
		if (node.left is None) and (node.right is None):
			if parentNode is None:
				return
			elif parentNode.left == node:
				parentNode.left = None
			else:
				parentNode.right = None
		elif node.left is None:
			if parentNode is None:
				node.value = node.right.value
				node.right = node.right.right
				node.left = node.right.left
			elif parentNode.left == node:
				parentNode.left = node.right
			else:
				parentNode.right = node.right
		elif node.right is None:
			if parentNode is None:
				node.value = node.left.value
				node.right = node.left.right
				node.left = node.left.left				
			elif parentNode.left == node:
				parentNode.left = node.left
			else:
				parentNode.right = node.left
		else:
			node.value = node.right.minValue()
			node.right.remove(node.value, node)
	
	def minValue(self):
		node = self

		while node.left is not None:
			node = node.left

		return node.value
