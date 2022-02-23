def phoneNumberMnemonics(phoneNumber):
    strings = []
    keypad = {'0': '', '1': '', '2': 'abc',
              '3': 'def', '4':'ghi', '5': 'jkl',
              '6': 'mno', '7': 'pqrs', '8': 'tuv',
              '9': 'wxyz'}
    
    queue = [(0, [])]
    
    while len(queue) > 0:
        phoneNumberIndex, letters = queue.pop(0)
        
        if phoneNumberIndex == len(phoneNumber):
            strings.append(''.join(letters))
        else:
            if keypad[phoneNumber[phoneNumberIndex]] == '':
                letters.append(phoneNumber[phoneNumberIndex])
                queue.append((phoneNumberIndex + 1, letters))
            else:
                for letter in keypad[phoneNumber[phoneNumberIndex]]:
                    newLetters = letters[:]
                    newLetters.append(letter)
                    queue.append((phoneNumberIndex + 1, newLetters))
    
    return strings
