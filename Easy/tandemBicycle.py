def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	speed = 0
	redShirtSpeeds = sorted(redShirtSpeeds)
	
	if fastest:
		blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=True)
	else:
		blueShirtSpeeds = sorted(blueShirtSpeeds)
		
	for i in range(len(redShirtSpeeds)):
		speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
		
	return speed
