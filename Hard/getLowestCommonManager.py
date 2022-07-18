def getLowestCommonManager(topManager, reportOne, reportTwo):
    commonManagers = []
    lcmHelper(topManager, reportOne, reportTwo, 0, commonManagers)
    return commonManagers[0]

def lcmHelper(topManager, reportOne, reportTwo, foundCount, commonManagers):
    foundCountCopy = foundCount
    
    for directReport in topManager.directReports:
        if foundCount < 2:
            foundCount += lcmHelper(directReport, reportOne, reportTwo, foundCountCopy, commonManagers)

    if topManager.name in [reportOne.name, reportTwo.name]:
        foundCount += 1

    if foundCount == 2:
        commonManagers.append(topManager)

    return foundCount
        
    
    
    # This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
