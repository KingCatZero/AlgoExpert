def reverseWordsInString(string):
    words = []
    isChar = True
    j = 0
    
    for i in range(len(string)):
                
        if (isChar and (string[i] == ' ')) or (not isChar and (string[i] != ' ')):
            words.append(string[j : i])
            isChar = not isChar
            j = i
                
    if j <= len(string) - 1:
        words.append(string[j :])
		
    return ''.join(words[:: -1])
