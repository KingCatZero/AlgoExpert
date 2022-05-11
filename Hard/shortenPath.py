def shortenPath(path):
    stack = []
    tokens = usefulTokens(path)
    isCurRoot = isCurrentlyRoot(path, stack)
    
    for token in tokens:
        if token == '..':
            if not isCurRoot:
                if (len(stack) == 0) or (stack[-1] == '..'):
                    stack.append('..')
                else:
                    stack.pop()
        else:
            stack.append(token)
            
        isCurRoot = isCurrentlyRoot(path, stack)
    
    if path[0] == '/':
        newPath = '/' + '/'.join(stack)
    else:
        newPath = '/'.join(stack)
        
    return newPath

def isCurrentlyRoot(path, stack):
    return (len(stack) == 0) and (path[0] == '/')
    
def usefulTokens(path):
    return list(filter(lambda token: token not in ['', '.'], path.split('/')))
