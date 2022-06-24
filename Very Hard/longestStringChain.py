def longestStringChain(strings):
    strings = sorted(strings, key = lambda s: len(s))
    lookup = {}
    head = ''
    
    for string in strings:
        lookup[string] = [0, '']
        
    for string in strings:
        longestChain = ''
        
        for i in range(len(string)):
            substring = string[: i] + string[i + 1 :]
            
            if substring in lookup:
                if (longestChain == '') or (lookup[substring][0] > lookup[longestChain][0]):
                    longestChain = substring
                    
        if longestChain != '':
            lookup[string] = [lookup[longestChain][0] + 1, longestChain]
            
            if (head == '') or (lookup[string][0] > lookup[head][0]):
                head = string
                
    return stringChain(lookup, head)
    
def stringChain(substringLookup, headOfChain):
    output = []
    
    while headOfChain != '':
        output.append(headOfChain)
        headOfChain = substringLookup[headOfChain][1]
    
    return output
