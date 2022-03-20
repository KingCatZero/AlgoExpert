def largestRange(array):
    largestInterval = [array[0], array[0]]
    lookup = {}
    
    for a in array:
        lookup[a] = False
        
    for a in array:
        if not lookup[a]:
            queue = [(a, 'l'), (a, 'r')]

            while len(queue) > 0:
                n, direction = queue.pop()
                lookup[n] = True

                if direction == 'l':
                    if n - 1 in lookup:
                        queue.append((n - 1, 'l'))
                    else:
                        l = n
                else:
                    if n + 1 in lookup:
                        queue.append((n + 1, 'r'))
                    else:
                        r = n

            if r - l > largestInterval[1] - largestInterval[0]:
                largestInterval = [l, r]
            
    return largestInterval
