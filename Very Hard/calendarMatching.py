def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    matches = []
    calendar1.insert(0, [dailyBounds1[0], dailyBounds1[0]])
    calendar1.append([dailyBounds1[1], dailyBounds1[1]])
    calendar2.insert(0, [dailyBounds2[0], dailyBounds2[0]])
    calendar2.append([dailyBounds2[1], dailyBounds2[1]])
    index1 = 0
    index2 = 0
    
    while notEndOfDay(calendar1, index1) and notEndOfDay(calendar2, index2):
        start1 = timeToMinutes(calendar1[index1][1])
        end1 = timeToMinutes(calendar1[index1 + 1][0])
        start2 = timeToMinutes(calendar2[index2][1])
        end2 = timeToMinutes(calendar2[index2 + 1][0])
        overlap = overlappingBound(start1, end1, start2, end2, meetingDuration)
        
        if len(overlap) > 0:
            matches.append(overlap)
            
        if end1 <= end2:
            index1 += 1
        else:
            index2 += 1
            
    return matches
        
def overlappingBound(start1, end1, start2, end2, meetingDuration):
    start = max(start1, start2)
    end = min(end1, end2)
    
    if (end - start) >= meetingDuration:
        return [minutesToTime(start), minutesToTime(end)]
    
    return []

def notEndOfDay(calendar, index):
    return index < len(calendar) - 1
    
def timeToMinutes(string):
    parts = string.split(':')
    return (int(parts[0]) * 60) + int(parts[1])

def minutesToTime(m):
    return '{}:{}{}'.format(m // 60, m % 60, '0' * (2 - len(str(m % 60))))
