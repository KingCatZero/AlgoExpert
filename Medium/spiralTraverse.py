def spiralTraverse(array):
	flatArray = []
	m = len(array[0])
	n = len(array)
	
	if min(m, n) % 2 == 0:
		mid = min(m, n) // 2
	else:
		mid = (min(m, n) + 1) // 2
	
	for i in range(mid):
		for j in range(i, m - i):
			flatArray.append(array[i][j])
			
		for j in range(i + 1, n - i - 1):
			flatArray.append(array[j][m - i - 1])
			
		if i * 2 < n - 1:
			for j in range(m - i - 1, i - 1, -1):
				flatArray.append(array[n - i - 1][j])
				
		if i * 2 < m - 1:
			for j in range(n - i - 2, i, -1):
				flatArray.append(array[j][i])
		
	return flatArray
