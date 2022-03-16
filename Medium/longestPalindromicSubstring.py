def longestPalindromicSubstring(string):
    for i in range(len(string), 1, -1):
        for j in range(len(string) - i + 1):
            if isPalindrome(string[j : j + i]):
                return string[j : j + i]
            
    return string[0]
        
def isPalindrome(string):
    return string == string[:: -1]
