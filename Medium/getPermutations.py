def getPermutations(array):
    perms = []
    getPermutationsHelper(0, array, perms)
    return perms

def getPermutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(list(array))
        return
        
    for j in range(i, len(array)):
        swap(array, i, j)
        getPermutationsHelper(i + 1, array, permutations)
        swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
