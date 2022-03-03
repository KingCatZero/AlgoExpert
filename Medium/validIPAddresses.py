def validIPAddresses(string):
    addresses = []
    validIPAddressesHelper(string, 0, 3, addresses)
    return addresses

def validIPAddressesHelper(string, start, dotCount, array):
    if dotCount == 0:
        if isValidSubstring(string[start :]):
            array.append(string)
        
        return
    
    for i in range(1, 4):
        if isValidSubstring(string[start : start + i]):
            newString = '{}.{}'.format(string[: start + i], string[start + i :])
            validIPAddressesHelper(newString, start + i + 1, dotCount - 1, array)
    
def isValidSubstring(string):
    if len(string) < 2:
        return len(string) == 1
    elif len(string) == 2:
        return string[0] != '0'
    
    return (string[0] != '0') and (int(string) <= 255)
