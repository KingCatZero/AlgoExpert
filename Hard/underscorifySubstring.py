def underscorifySubstring(string, substring):
    output = []
    intervals = []
    substringLength = len(substring)
    stringLength = len(string)
    
    for i in range(stringLength):
        if isMatch(string, stringLength, substring, substringLength, i):
            intervals.append((i, i + substringLength))
            
    collapsedIntervals = packIntervals(intervals)
    i = 0
    j = 0
    
    if len(collapsedIntervals) == 0:
        return string
    
    while (i < stringLength) and (j < len(collapsedIntervals)):
        if i == collapsedIntervals[j][0]:
            start = collapsedIntervals[j][0]
            end = collapsedIntervals[j][1]
            output.append('_' + string[start : end] + '_')
            i = end
            j += 1
        else:
            output.append(string[i])
            i += 1
            
    output.append(string[i :])            
    return ''.join(output)

            
    
def isMatch(string, stringLength, substring, substringLength, i):
    if i <= stringLength - substringLength:
        return string[i : i + substringLength] == substring
    
    return False

def packIntervals(intervals):
    if len(intervals) < 2:
        return intervals
    
    output = []
    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            output.append((start, end))
            start = intervals[i][0]
            
        end = intervals[i][1]
            
    output.append((start, end))
    return output
