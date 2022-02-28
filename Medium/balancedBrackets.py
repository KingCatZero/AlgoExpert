def balancedBrackets(string):
    stack = []
    lookup = {')':'(', ']':'[', '}':'{'}
    
    for c in string:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if (len(stack) == 0) or (lookup[c] != stack[-1]):
                return False
            else:
                stack.pop()
        
    return len(stack) == 0
