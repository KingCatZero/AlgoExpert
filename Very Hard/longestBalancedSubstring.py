def longestBalancedSubstring(string):
    maxLength = 0
    length = 0
    gap = 0
    gapLengths = [0] * (len(string) + 1)
    
    for c in string:
        if c == '(':
            gap += 1
            length = 0
            gapLengths[gap] = 0
        elif gap > 0:
            length = gapLengths[gap] + 2
            gap -= 1
            gapLengths[gap] += length
            maxLength = max(maxLength, gapLengths[gap])
        else:
            gap = 0
            length = 0
            gapLengths[0] = 0
        
    return maxLength
