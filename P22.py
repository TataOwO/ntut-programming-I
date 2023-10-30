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
    
    # straight flush
    if straight and len(cardDict.keys()) == 1: return 9
    
    # four of a kind
    if max(countArray) == 4: return 8
    
    # full house
    if max(countArray) == 3 and min(countArray) == 2: return 7
    
    # flush
    if len(cardDict.keys()) == 1: return 6
    
    # straight
    if straight: return 5
    
    # three of a kind
    if max(countArray) == 3: return 4
    
    # two pairs
    if countArray.count(2) == 2: return 3
    
    # one pair
    if countArray.count(2) == 1: return 2
    
    # high card
    return 1

def determineErrorInput(numTable, cardArray, shapeArray, numArray, cardDict):
    possibleShapes = "SHDC"
    possibleNumbers = numTable.keys()
    # print(list(possibleNumbers))
    
    # error input
    for each in set(shapeArray):
        if each not in possibleShapes: return -1
    
    # error input
    for each in set(numArray):
        if each not in possibleNumbers: return -1
    
    return 0

def processCardInput(cardArray):
    numTable = {str(x):x for x in range(2, 11)}
    numTable.update({"A":1, "J":11, "Q":12, "K":13})
    
    shapeArray = [x[-1] for x in cardArray] # array of shapes
    numArray = [x[:-1] for x in cardArray] # array of numbers
    
    # create a dict with keys being the shapes and values being array of the numbers
    cardDict = dict.fromkeys(shapeArray)
    for key in cardDict: cardDict[key] = []
    
    for index, each in enumerate(shapeArray):
        cardDict[each].append(numArray[index])
        
    # calculate the amount of appearance of each number
    countArray = [numArray.count(x) for x in set(numArray)]
    
    # find errors
    errorCode = determineErrorInput(numTable, cardArray, shapeArray, numArray, cardDict)
    
    if errorCode: return errorCode
    
    # find score
    return determineStatus(numTable, cardArray, shapeArray, numArray, cardDict, countArray)

def main():
    scoreArray = []
    foundCards = []
    for c in range(int(input())):
        inp = input().split(" ")
        scoreArray.append([inp[0], processCardInput(inp[1:])])
        foundCards.extend(inp[1:])
    scoreArray.sort(key=lambda x: x[1], reverse=True)
    
    # print(scoreArray)
    
    if scoreArray[-1][1] == -1:
        print("Error input")
        return
    if len(foundCards) != len(set(foundCards)):
        print("Duplicate deal")
        return
    
    for each in scoreArray: print(each[0], each[1])

if __name__ == "__main__":
    main()
