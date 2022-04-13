# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
		
	def setFirstNode(self, node):
		self.head = node
		self.tail = node

    def setHead(self, node):		
		if self.head is None:
			self.setFirstNode(node)
		else:
			head = self.head
			self.insertBefore(head, node)

    def setTail(self, node):
		if self.tail is None:
			self.setFirstNode(node)
		else:
			tail = self.tail
			self.insertAfter(tail, node)

    def insertBefore(self, node, nodeToInsert):
		self.remove(nodeToInsert)
		
		if node == self.head:
			self.head = nodeToInsert
			
		nodePrev = node.prev
		self.rebindNext(nodePrev, nodeToInsert)
		self.rebindPrev(nodeToInsert, nodePrev)
		self.rebindNext(nodeToInsert, node)
		self.rebindPrev(node, nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
		self.remove(nodeToInsert)
		
		if node == self.tail:
			self.tail = nodeToInsert
			
		nodeNext = node.next
		self.rebindNext(node, nodeToInsert)
		self.rebindPrev(nodeToInsert, node)
		self.rebindNext(nodeToInsert, nodeNext)
		self.rebindPrev(nodeNext, nodeToInsert)

    def insertAtPosition(self, position, nodeToInsert):		
		if self.head is None:
			self.setFirstNode(nodeToInsert)
		else:		
			node = self.head
			i = 1

			while i < position:
				i += 1
				node = node.next

			self.insertBefore(node, nodeToInsert)
				
    def removeNodesWithValue(self, value):
        node = self.head
		
		while node is not None:
			if node.value == value:
				nodeToRemove = node
				node = node.next
				self.remove(nodeToRemove)
			else:
				node = node.next

    def remove(self, node):			
		nodePrev = node.prev
		nodeNext = node.next
		
		if (node == self.head) and (node == self.tail):
			self.setFirstNode(None)
		elif node == self.head:
			self.head = nodeNext
			self.rebindPrev(nodeNext, None)
		elif node == self.tail:
			self.tail = nodePrev
			self.rebindNext(nodePrev, None)
		else:
			self.rebindNext(nodePrev, nodeNext)
			self.rebindPrev(nodeNext, nodePrev)
			
		self.rebindNext(node, None)
		self.rebindPrev(node, None)
			
	def rebindPrev(self, node, nodeToBind):
		if node is not None:
			node.prev = nodeToBind
		
	def rebindNext(self, node, nodeToBind):
		if node is not None:
			node.next = nodeToBind

    def containsNodeWithValue(self, value):
        node = self.head
		
		while node is not None:
			if node.value == value:
				return True
			else:
				node = node.next
			
		return False
