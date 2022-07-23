def ambiguousMeasurements(measuringCups, low, high):
    return ambiguousMeasurementsHelper(measuringCups, low, high, {})

def ambiguousMeasurementsHelper(measuringCups, low, high, rangeLookup):    
    if (low < 0) and (high < 0):
        return False
    elif (low, high) in rangeLookup:
        return rangeLookup[(low, high)]
    
    canMeasure = False
    
    for i in range(len(measuringCups)):
        cupLow, cupHigh = measuringCups[i]
        
        if (cupLow >= low) and (cupHigh <= high):
            canMeasure = True
            break
        else:
            canMeasure = ambiguousMeasurementsHelper(measuringCups, low - cupLow, high - cupHigh, rangeLookup)
            
            if canMeasure:
                break
    
    rangeLookup[(low, high)] = canMeasure
    return canMeasure
