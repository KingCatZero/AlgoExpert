def caesarCipherEncryptor(string, key):
	array = [''] * len(string)
    letters = 'abcdefghijklmnopqrstuvwxyz'
	letterLookup = {}
	
	for i in range(26):
		letterLookup[letters[i]] = i
	
	for i in range(len(string)):
		j = (letterLookup[string[i]] + key) % 26
		array[i] = letters[j]
		
	return ''.join(array)
