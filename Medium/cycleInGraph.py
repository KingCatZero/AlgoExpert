def cycleInGraph(edges):
    colours = [0] * len(edges)
    
    for i in range(len(edges)):
        cycleInGraphHelper(edges, colours, i)
		
    return sum(colours) < (len(colours) * 2)
    
def cycleInGraphHelper(edges, colours, i):
    if colours[i] > 0:
        return
    
    colours[i] = 1
    
    for j in edges[i]:
        if colours[j] == 1:
            return
        else:
            cycleInGraphHelper(edges, colours, j)
    
    colours[i] = 2

