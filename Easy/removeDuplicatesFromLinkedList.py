# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
	nextNode = linkedList.next
	
	while True:
		if nextNode is None:
			node.next = None
			return linkedList
		elif nextNode.value == node.value:
			nextNode = nextNode.next
		else:
			node.next = nextNode
			node = nextNode
			nextNode = node.next
