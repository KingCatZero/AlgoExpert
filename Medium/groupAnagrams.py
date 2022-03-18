def groupAnagrams(words):
    groups = {}
    
    for i in range(len(words)):
        group = ''.join(sorted(words[i]))
        
        if group in groups:
            groups[group].append(words[i])
        else:
            groups[group] = [words[i]]
        
    return list(groups.values())
