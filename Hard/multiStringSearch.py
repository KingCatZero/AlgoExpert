class Node():
    def __init__(self, value, wordNumber):
        self.value = value
        self.wordNumber = wordNumber
        self.suffixes = {}
        
class Trie():
    def __init__(self, words):
        self.head = Node('*', -1)
        
        for i in range(len(words)):
            node = self.head
            
            for j in range(len(words[i]) - 1):
                c = words[i][j]
                
                if c not in node.suffixes:
                    node.suffixes[c] = Node(c, -1)
                    
                node = node.suffixes[c]
            
            c = words[i][-1]
            
            if c in node.suffixes:
                node.suffixes[c].wordNumber = i
            else:
                node.suffixes[c] = Node(c, i)

def multiStringSearch(bigString, smallStrings):
    output = [False] * len(smallStrings)
    trie = Trie(smallStrings)
    
    for i in range(len(bigString)):
        node = trie.head
        
        for j in range(i, len(bigString)):            
            if bigString[j] in node.suffixes:
                node = node.suffixes[bigString[j]]
                
                if node.wordNumber >= 0:
                    output[node.wordNumber] = True
            else:
                break
    
    return output
