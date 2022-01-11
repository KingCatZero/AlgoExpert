def runLengthEncoding(string):
    array = []
    count = 0
    
    for i in range(len(string) - 1):
        count += 1
        
        if count == 9:
            array.append('9' + string[i])
            count = 0
        elif string[i] != string[i + 1]:
            array.append(str(count) + string[i])
            count = 0
    
    if count == 0:
        array.append('1' + string[-1])
    else:
        array.append(str(count + 1) + string[-1])
        
    return ''.join(array)
