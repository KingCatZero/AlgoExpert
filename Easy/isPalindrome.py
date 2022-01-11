def isPalindrome(string):
	l = len(string) - 1
	
    for i in range(len(string)):
		if string[i] != string[l - i]:
			return False
		
	return True
