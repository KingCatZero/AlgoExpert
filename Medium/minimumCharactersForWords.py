def minimumCharactersForWords(words):
    charSpan = []
    charCount = {}
    
    for word in words:
        currentCharCount = {}
        
        for c in word:
            if c in currentCharCount:
                currentCharCount[c] += 1
            else:
                currentCharCount[c] = 1
            
        for c in currentCharCount:            
            if c in charCount:
                charCount[c] = max(charCount[c], currentCharCount[c])
            else:
                charCount[c] = currentCharCount[c]
                
    for c in charCount:
        for count in range(charCount[c]):
            charSpan.append(c)
    
    return charSpan
