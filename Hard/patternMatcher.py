def patternMatcher(pattern, string):
    patChars = patternElements(pattern)
    patCharCounts = patternElementCounts(patChars)
    xLengthMax = (len(string) // patCharCounts['x']) + 1
    
    for xLength in range(1, xLengthMax):
        if 'y' in patCharCounts:
            yLength = (len(string) - (xLength * patCharCounts['x'])) // patCharCounts['y']
        else:
            yLength = 0
        
        patCharLengths = {'x': xLength, 'y': yLength}
        substringLookup = {}
        index = 0
        
        for c in patChars:
			if c not in substringLookup:
                substringLookup[c] = string[index : index + patCharLengths[c]]
            elif substringLookup[c] != string[index : index + patCharLengths[c]]:
                break
                
            index += patCharLengths[c]
            
        if index == len(string):
            return matchedSubstrings(substringLookup, pattern[0] == 'y')
		
	return []
        
def matchedSubstrings(substringLookup, patternCharsSwapped):
    if patternCharsSwapped:
        if 'y' in substringLookup:
            return [substringLookup['y'], substringLookup['x']]
        else:
            return ['', substringLookup['x']]
    else:
        if 'y' in substringLookup:
            return [substringLookup['x'], substringLookup['y']]
        else:
            return [substringLookup['x'], '']
        
def patternElements(pattern):
    if pattern[0] == 'x':
        return list(pattern)
    
    charMap = {'x': 'y', 'y': 'x'}
    return list(map(lambda c: charMap[c], list(pattern)))

def patternElementCounts(pattern):
    counts = {}
    
    for c in pattern:
        if c not in counts:
            counts[c] = 0
            
        counts[c] += 1
    
    return counts
