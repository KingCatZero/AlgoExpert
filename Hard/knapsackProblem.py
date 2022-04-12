def knapsackProblem(items, capacity):
	if capacity == 0:
		return [0, []]
	
	values = knapsackValues(items, capacity)    
    return [values[-1][-1], unpack(items, capacity, values)]

def knapsackValues(items, capacity):
	row = [0] * (capacity + 1)
	values = [row[:] for i in range(len(items) + 1)]
    
    for i in range(1, len(values)):
        v, w = items[i - 1]
        
        for j in range(w):
            values[i][j] = values[i - 1][j]
        
        for j in range(w, capacity + 1):
            values[i][j] = max(values[i - 1][j], values[i - 1][j - w] + v)
		
	return values

def unpack(items, capacity, values):
	chosenItems = []
	j = capacity
    
    for i in range(len(values) - 1, 0, -1):
        if values[i][j] > values[i - 1][j]:
            chosenItems.append(i - 1)
            j = j - items[i - 1][1]
			
	return chosenItems
