class Node():
    def __init__(self, letter):
        self.letter = letter
        self.prefix = ''
        self.isEndOfWord = False
        self.children = {}
        
    def addLetter(self, letter):
        self.children[letter] = Node(letter)
        
class Trie():
    def __init__(self):
        self.root = Node('ROOT')
        
    def addWord(self, word):
        node = self.root
        prefix = []
        
        for c in word:
            if c not in node.children:
                node.addLetter(c)
                
            node = node.children[c]
            
        node.isEndOfWord = True
        node.prefix = word
            
def boggleBoard(board, words):
    output = set()
    trie = Trie()
    queue = []
    height = len(board)
    width = len(board[0])
    
    for word in words:
        trie.addWord(word)
    
    for i in range(height):
        for j in range(width):
            if board[i][j] in trie.root.children:
                queue.append((trie.root.children[board[i][j]], set([(i, j)]), i, j))
             
    while len(queue) > 0:
        node, visitedNodes, row, col = queue.pop(0)
        
        if node.isEndOfWord:
            output.add(node.prefix)
            
        for i, j in neighbours(row, col, height, width):
            if board[i][j] in node.children:
                if (i, j) not in visitedNodes:
                    visitedNodesCopy = visitedNodes.copy()
                    visitedNodesCopy.add((i, j))
                    queue.append((node.children[board[i][j]], visitedNodesCopy, i, j))
    
    return output
    
def neighbours(x, y, m, n):
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if (0 <= x + dx < m) and (0 <= y + dy < n):
            yield (x + dx, y + dy)
