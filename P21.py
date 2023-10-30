def determineStaight(numTable, numArray):
    numArray.sort(key=lambda x: numTable[x])
    straight = False
    straightFlush = False
    if "".join(numArray) in "A2345678910JQK": return True
    for i in "A234":
        if i == numArray[0]: numArray.append(numArray.pop(0))
    if "".join(numArray) in "10JQKA234": return True
    return False

def determineStatus(numTable, cardArray, shapeArray, numArray, cardDict, countArray):
    straight = determineStaight(numTable, numArray.copy())
    
    if straight and len(cardDict.keys()) == 1: return 9
    
    if max(countArray) == 4: return 8
    
    if max(countArray) == 3 and min(countArray) == 2: return 7
    
    if len(cardDict.keys()) == 1: return 6
    
    if straight: return 5
    
    if max(countArray) == 3: return 4
    
    if countArray.count(2) == 2: return 3
    
    if countArray.count(2) == 1: return 2
    
    return 1

def determineErrorInput(numTable, cardArray, shapeArray, numArray, cardDict):
    possibleShapes = "SHDC"
    possibleNumbers = numTable.keys()
    # print(list(possibleNumbers))
    
    for each in set(shapeArray):
        if each not in possibleShapes: return 1
    
    for each in set(numArray):
        if each not in possibleNumbers: return 1
    
    for key in cardDict:
        if len(cardDict[key]) != len(set(cardDict[key])): return 2
    
    return 0

def main():
    numTable = {str(x):x for x in range(2, 11)}
    numTable.update({"A":1, "J":11, "Q":12, "K":13})
    
    cardArray = input().split()
    shapeArray = [x[-1] for x in cardArray] # array of shapes
    numArray = [x[:-1] for x in cardArray] # array of numbers
    
    # create a dict with keys being the shapes and values being array of the numbers
    cardDict = dict.fromkeys(shapeArray)
    for key in cardDict: cardDict[key] = []
    
    for index, each in enumerate(shapeArray):
        cardDict[each].append(numArray[index])
        
    # calculate the amount of appearance of each number
    countArray = [numArray.count(x) for x in set(numArray)]
    
    errorCode = determineErrorInput(numTable, cardArray, shapeArray, numArray, cardDict)
    
    if errorCode:
        if errorCode == 1: print("Error input")
        if errorCode == 2: print("Duplicate deal")
        return
    
    print(determineStatus(numTable, cardArray, shapeArray, numArray, cardDict, countArray))

if __name__ == "__main__":
    main()
