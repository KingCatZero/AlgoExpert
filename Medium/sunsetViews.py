def sunsetViews(buildings, direction):
    views = []
    maxHeight = -1
    
    if direction == 'EAST':
        indexRange = range(len(buildings) - 1, -1, -1)
    else:
        indexRange = range(len(buildings))
        
    for i in indexRange:
        if buildings[i] > maxHeight:
            views.append(i)
        
        maxHeight = max(maxHeight, buildings[i])
    
    if direction == 'EAST':
        views = views[:: -1]
        
    return views
