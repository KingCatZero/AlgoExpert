def longestSubstringWithoutDuplication(string):
    lookup = {}
    start = 0
    end = 0
    j = 0
    
    for i in range(len(string)):
        k = lookupValue(lookup, string[i])
        
        if k != -1:
            start, end = longestInterval(start, end, j, i)
            resetLookup(lookup, string, k)
            j = k + 1
            
        lookup[string[i]] = i
        
    start, end = longestInterval(start, end, j, len(string))
    return string[start : end]

def lookupValue(lookup, c):
    if c in lookup:
        return lookup[c]
    
    return -1

def resetLookup(lookup, string, k):
    for i in range(k + 1):
        if lookup[string[i]] < k:
            lookup[string[i]] = -1

def longestInterval(start, end, i, j):
    if end - start < j - i:
        return i, j
    
    return start, end
