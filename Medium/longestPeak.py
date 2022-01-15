def longestPeak(array):
    if len(array) < 3:
		return 0
	
	sign = 0
	peak = 1
	maxPeak = 0
	
	for i in range(1, len(array)):
		if array[i] == array[i - 1]:
			if sign == -1:
				maxPeak = max(maxPeak, peak)
				
			sign = 0
			peak = 1
		elif array[i] < array[i - 1]:
			if sign == 1:
				sign = -1
				peak += 1
			elif sign == -1:
				peak += 1
		else:
			if sign == 0:
				sign = 1
			elif sign == -1:
				maxPeak = max(maxPeak, peak)
				sign = 1
				peak = 1
				
			peak += 1
			
	if sign == -1:
		maxPeak = max(maxPeak, peak)
		
	return maxPeak
