def rectangleMania(coords):    
    count = 0
    diagonalPairLookup = set()
    
    for i in range(len(coords)):
        x1, y1 = coords[i]
        cornerLookup = set()
        
        for j in range(len(coords)):
            x2, y2 = coords[j]
            
            if ((x1, y2) in cornerLookup) and ((x2, y1) in cornerLookup):
                pair = tuple(sorted([(x1, y1), (x2, y2)]))
                
                if pair not in diagonalPairLookup:
                    count += 1
                    diagonalPairLookup.add(pair)
                    
            cornerLookup.add((x2, y2))
    
    return count
