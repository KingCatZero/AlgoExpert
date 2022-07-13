class Node():
    def __init__(self, number, visitedFrom, visitOrder, minVisitOrder):
        self.number = number
        self.visitedFrom = visitedFrom
        self.visitOrder = visitOrder
        self.minVisitOrder = minVisitOrder

def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True
    
    nodes = [Node(i, -1, -1, -1) for i in range(len(edges))]
    twoEdgeConnectedGraphHelper(edges, nodes, 0, 0, 0)
    return not hasBridgeOrDisconnect(nodes)

def twoEdgeConnectedGraphHelper(edges, nodes, i, visitedFrom, visitOrder):
    nodes[i].visitedFrom = visitedFrom
    nodes[i].visitOrder = visitOrder
    nodes[i].minVisitOrder = visitOrder
    
    for j in edges[i]:
        if j != nodes[i].visitedFrom:
            if nodes[j].visitOrder == -1:
                nodes[i].minVisitOrder = min(nodes[i].minVisitOrder, twoEdgeConnectedGraphHelper(edges, nodes, j, i, visitOrder + 1))
            elif nodes[j].visitOrder < nodes[i].visitOrder:
                nodes[i].minVisitOrder = min(nodes[i].minVisitOrder, nodes[j].visitOrder)
            
    return nodes[i].minVisitOrder

def hasBridgeOrDisconnect(nodes):
    for node in nodes:
        if node.number > 0:
            if (node.visitOrder == -1) or (node.visitOrder == node.minVisitOrder):
                return True
            
    return False
