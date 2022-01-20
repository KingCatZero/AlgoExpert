def mergeOverlappingIntervals(intervals):
	if len(intervals) < 2:
		return intervals
	
  intervals = sorted(intervals, key = lambda x: x[0])
	overlappingIntervals = []
	
	while len(intervals) > 0:
		interval = intervals.pop(0)
		
		if len(overlappingIntervals) == 0:
			overlappingIntervals.append(interval)
		elif interval[0] <= overlappingIntervals[-1][1]:
			if interval[1] > overlappingIntervals[-1][1]:
				overlappingIntervals[-1][1] = interval[1]
		else:
			overlappingIntervals.append(interval)
			
	return overlappingIntervals
