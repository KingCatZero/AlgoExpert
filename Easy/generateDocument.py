def generateDocument(characters, document):
    characterLookup = {}
	
	for c in characters:
		if c in characterLookup:
			characterLookup[c] += 1
		else:
			characterLookup[c] = 1
			
	for c in document:
		if (c not in characterLookup) or (characterLookup[c] == 0):
			return False
		else:
			characterLookup[c] -= 1
	
	return True
