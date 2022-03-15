def sortStack(stack):
    array = []
	
	while len(stack) > 0:
		array.append(stack.pop())
		
	for i in range(1, len(array)):
		for j in range(i, 0, -1):
			if array[j] < array[j - 1]:
				array[j], array[j - 1] = array[j - 1], array[j]
				
	while len(array) > 0:
		stack.append(array.pop(0))
		
	return stack
