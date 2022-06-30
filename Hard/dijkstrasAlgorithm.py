class Node():
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.distance = float('inf')
        self.visited = False

class MinHeap():
    def __init__(self):
        self.array = []
    
    def parentIndex(self, i):
        return int((i - 1) / 2)
    
    def leftChildIndex(self, i):
        return (i * 2) + 1
    
    def rightChildIndex(self, i):
        return (i * 2) + 2
    
    def siftUp(self):
        i = len(self.array) - 1
        
        while i > 0:
            p = self.parentIndex(i)
            
            if self.array[p].distance > self.array[i].distance:
                self.array[p], self.array[i] = self.array[i], self.array[p]
                i = p
            else:
                break
    
    def siftDown(self):
        i = 0
        
        while i < len(self.array):
            l = self.leftChildIndex(i)
            r = self.rightChildIndex(i)
            
            if (l < len(self.array)) and (r < len(self.array)):
                if self.array[l].distance <= self.array[r].distance:
                    c = l
                else:
                    c = r
            elif l < len(self.array):
                c = l
            else:
                break
                
            if self.array[i].distance > self.array[c].distance:
                self.array[c], self.array[i] = self.array[i], self.array[c]
                i = c
            else:
                break

    def insert(self, x):
        self.array.append(x)
        self.siftUp()
    
    def remove(self):
        x = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.siftDown()
        return x

def dijkstrasAlgorithm(start, edges):
    distances = [0] * len(edges)
    nodes = buildNetwork(edges)
    nodes[start].distance = 0
    heap = MinHeap()
    heap.insert(nodes[start])
    
    while len(heap.array) > 0:
        node = heap.remove()
        node.visited = True
        
        for edge, distanceToEdge in node.edges:
            if not edge.visited:
                if node.distance + distanceToEdge < edge.distance:
                    edge.distance = node.distance + distanceToEdge
                    heap.insert(edge)
                    
    return networkTotalDistances(nodes)

def networkTotalDistances(nodes):
    return list(map(lambda node: node.distance if node.distance < float('inf') else -1, nodes))

def buildNetwork(edges):
    nodes = []
    
    for i in range(len(edges)):
        nodes.append(Node(i))
        
    for i in range(len(edges)):
        for destination, distance in edges[i]:
            nodes[i].edges.append((nodes[destination], distance))
    
    return nodes
