def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights = sorted(redShirtHeights)
	blueShirtHeights = sorted(blueShirtHeights)
	
	if redShirtHeights[-1] == blueShirtHeights[-1]:
		return False
	elif redShirtHeights[-1] < blueShirtHeights[-1]:
		for i in range(len(redShirtHeights)):
			if redShirtHeights[i] >= blueShirtHeights[i]:
				return False
	else:
		for i in range(len(redShirtHeights)):
			if redShirtHeights[i] <= blueShirtHeights[i]:
				return False
			
	return True
