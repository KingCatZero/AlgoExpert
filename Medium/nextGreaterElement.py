def nextGreaterElement(array):
	if len(array) == 0:
		return []
	
    outputArray = [-1] * len(array)
    stack = [0]
    
    for i in range(len(array)):
        while (len(stack) > 0) and (array[stack[-1]] < array[i]):
            j = stack.pop()
            outputArray[j] = array[i]
            
        stack.append(i)
    
    for i in range(stack[0] + 1):
        while array[stack[-1]] < array[i]:
            j = stack.pop()
            outputArray[j] = array[i]
            
    return outputArray
