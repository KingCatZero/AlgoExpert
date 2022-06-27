def knuthMorrisPrattAlgorithm(string, substring):
    pointers = buildPointers(substring)
    stringIndex = 0
    substringIndex = 0
    
    while stringIndex < len(string):
        if string[stringIndex] == substring[substringIndex]:
            stringIndex += 1
            substringIndex += 1
        elif substringIndex == 0:
            stringIndex += 1
        elif pointers[substringIndex - 1] == -1:
            substringIndex = 0
        else:
            substringIndex = pointers[substringIndex - 1] + 1
            
        if substringIndex == len(substring):
            return True
    
    return False
        
def buildPointers(substring):
    output = []
    charLookup = {}
    
    for i in range(len(substring)):
        if substring[i] in charLookup:
            output.append(charLookup[substring[i]])
        else:
            output.append(-1)
        
        charLookup[substring[i]] = i
        
    return output
    
