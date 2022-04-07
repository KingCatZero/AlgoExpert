def radixSort(array):
	if len(array) < 2:
		return array
	
    bounds = [(0, len(array))]
    q = 10 ** mostSignificantPosition(array)
    
    while q > 0:
        nextBounds = []
        
        for bound in bounds:
            i = bound[0]
			
            for bucket in buckets(array, bound[0], bound[1], q):
                length = len(bucket)
				
				for j in range(length):
					array[i + j] = bucket[j]

				if length > 1:
					nextBounds.append((i, i + length))

				i += length
					
        bounds = nextBounds[:]            
        q = q // 10
        
    return array

def buckets(array, l, r, q):
	nonEmptyDigits = []
    digits = [[] for i in range(10)]
    
    for i in range(l, r):
        d = significantDigit(array[i], q)
        digits[d].append(array[i])
        
    for i in range(10):
		if len(digits[i]) > 0:
			nonEmptyDigits.append(digits[i])
			
	return nonEmptyDigits

def mostSignificantPosition(array):
    return len(str(max(array))) - 1

def significantDigit(n, q):
    return int(n // q) % 10
