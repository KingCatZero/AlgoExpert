def smallestSubstringContaining(bigString, smallString):
    smallestCoveringString = ''
    coveredLettersCount = 0
    counts = letterCounts(smallString)
    l = -1
    
    for r in range(len(bigString)):
        if bigString[r] in counts:
            counts[bigString[r]][1] += 1
            
            if counts[bigString[r]][0] == counts[bigString[r]][1]:
                coveredLettersCount += 1
                
                if coveredLettersCount == len(counts):
                    while coveredLettersCount == len(counts):
                        l += 1
                        
                        if bigString[l] in counts:
                            counts[bigString[l]][1] -= 1
                            
                            if counts[bigString[l]][0] > counts[bigString[l]][1]:
                                coveredLettersCount -= 1
                    
                    if (smallestCoveringString == '') or (r - l + 1 < len(smallestCoveringString)):
                        smallestCoveringString = bigString[l : r + 1]
    
    return smallestCoveringString
                        

def letterCounts(string):
    counts = {}
    
    for c in string:
        if c not in counts:
            counts[c] = [0, 0]
            
        counts[c][0] += 1
    
    return counts
