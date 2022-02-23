# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	nodes = [descendantOne, descendantTwo]
    depths = [0, 0]
	
	for i in range(2):
		node = nodes[i]
		depth = 0
		
		while node.name != topAncestor.name:
			node = node.ancestor
			depth += 1
			
		depths[i] = depth
		
	while nodes[0].name != nodes[1].name:
		if depths[0] < depths[1]:
			nodes[1] = nodes[1].ancestor
			depths[1] -= 1
		else:
			nodes[0] = nodes[0].ancestor
			depths[0] -= 1
			
	return nodes[0]
