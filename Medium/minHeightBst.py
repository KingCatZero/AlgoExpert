def minHeightBst(array):
    sortedArray = []
	minHeightBstHelper(array, sortedArray, 0, len(array) - 1)
	node = BST(sortedArray[0])
	
	for i in range(1, len(sortedArray)):
		node.insert(sortedArray[i])
		
	return node

def minHeightBstHelper(array, newArray, l, r):
    mid = int((l + r) / 2)
    newArray.append(array[mid])
    
    if l < mid:
        minHeightBstHelper(array, newArray, l, mid - 1)
        
    if r > mid:
        minHeightBstHelper(array, newArray, mid + 1, r)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
