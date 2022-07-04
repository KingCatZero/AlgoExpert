class Node():
    def __init__(self, row, col, estimatedDistance):
        self.row = row
        self.col = col
        self.estimatedDistance = estimatedDistance
        self.distance = float('inf')
        self.visited = False
        self.prev = None

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

def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = buildGraphNodes(graph, endRow, endCol)
    nodes[startRow][startCol].distance = 0
    heap = MinHeap()
    heap.insert(nodes[startRow][startCol])
    
    while len(heap.array) > 0:
        currentNode = heap.remove()
        currentNode.visited = True
        
        if (currentNode.row == endRow) and (currentNode.col == endCol):
            break
        
        for rowNbr, colNbr in availableNeighbours(graph, currentNode.row, currentNode.col):
            node = nodes[rowNbr][colNbr]
            
            if not node.visited:
                if node.estimatedDistance + currentNode.distance < node.distance:
                    node.distance = node.estimatedDistance + currentNode.distance
                    node.prev = currentNode
                    heap.insert(node)
    
    return buildPathToEnd(nodes, nodes[endRow][endCol])

def buildPathToEnd(nodes, end):
    output = []
    
    if end.distance == float('inf'):
        return output
    
    while end is not None:
        output.append([end.row, end.col])
        end = end.prev
    
    return output[:: -1]

def buildGraphNodes(graph, endRow, endCol):
    graph = [row[:] for row in graph]
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            estimatedDistance = manhattanDistance(i, j, endRow, endCol)
            graph[i][j] = Node(i, j, estimatedDistance)
                
    return graph

def manhattanDistance(startRow, startCol, endRow, endCol):
    return abs(startRow - endRow) + abs(startCol - endCol)

def availableNeighbours(graph, row, col):
    points = []
    
    if (row > 0) and (graph[row - 1][col] == 0):
        points.append((row - 1, col))
        
    if (row < len(graph) - 1) and (graph[row + 1][col] == 0):
        points.append((row + 1, col))
        
    if (col > 0) and (graph[row][col - 1] == 0):
        points.append((row, col - 1))
        
    if (col < len(graph[0]) - 1) and (graph[row][col + 1] == 0):
        points.append((row, col + 1))
    
    return points
