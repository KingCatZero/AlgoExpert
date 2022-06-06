def diskStacking(disks):
    stacks = [-1] * len(disks)
    disks = sortedDisks(disks)
    
    for i in range(1, len(disks)):
        maxBaseForCurrentDisk = -1
        
        for j in range(i):
            if isBase(disks[i], disks[j]):
                if isMaxBaseForCurrentDisk(disks, maxBaseForCurrentDisk, j):
                    maxBaseForCurrentDisk = j
                    
        if maxBaseForCurrentDisk >= 0:
            disks[i][3] += disks[maxBaseForCurrentDisk][3]
            stacks[i] = maxBaseForCurrentDisk
            
    return bestDiskStack(disks, stacks)
    
def bestDiskStack(disks, stacks):
    bestStack = []
    maxCurrentStack = 0
    
    for i in range(1, len(disks)):
        if disks[i][3] > disks[maxCurrentStack][3]:
            maxCurrentStack = i
        
    i = maxCurrentStack
            
    while i >= 0:
        bestStack.append([disks[i][0], disks[i][1], disks[i][2]])
        i = stacks[i]
        
    return bestStack
    
def sortedDisks(disks):
    disks = list(map(lambda disk: [disk[0], disk[1], disk[2], disk[2]], disks))
    disks = sorted(disks, key = lambda disk: disk[0], reverse = True)
    return disks
            
def isBase(disk1, disk2):
    return (disk1[0] < disk2[0]) and (disk1[1] < disk2[1]) and (disk1[2] < disk2[2])

def isMaxBaseForCurrentDisk(disks, i, j):
    return (i == -1) or (disks[i][3] < disks[j][3])
