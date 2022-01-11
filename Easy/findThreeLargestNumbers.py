def findThreeLargestNumbers(array):
    nums = [None] * 3
	
	for a in array:
		for i in range(2, -1, -1):
			if nums[i] is None:
				nums[i] = a
				break
			elif nums[i] < a:
				for j in range(i):
					nums[j] = nums[j + 1]
					
				nums[i] = a			
				break				
	
	return nums
