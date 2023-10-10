# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE
# RANDOM GIBBERISH HERE

def validateClassName(name):
    if len(name) <= 4:
        return False
    if not name[-4:].isnumeric():
        return False
    return True

def validateClassHour(hour):
    if not hour.isnumeric():
        return False
    if int(hour) not in range(1, 4):
        return False
    return True

def validateClassTime(timeInp):
    if len(timeInp) != 2:
        return False
    if timeInp[0] not in "12345":
        return False
    if timeInp[1] not in "123456789abc":
        return False
    return True

def processInput():
    noError = True
    
    className = input()
    noError &= validateClassName(className)
    totalHour = input()
    noError &= validateClassHour(totalHour)
    totalHour = int(totalHour)
    
    outputDict = {className: []}
    
    for c in range(totalHour):
        classTime, errorCode = processClassTime()
        outputDict[className].append(classTime)
        noError &= errorCode
    
    return outputDict, noError

def processClassTime():
    classTime = input()
    noError = validateClassTime(classTime)
    return classTime, noError

def checkClassTimeError(classNameA, classNameB, classA, classB):
    notFound = True
    for classTime in classA:
        if classTime in classB:
            notFound = False
            formatPrint(classNameA, classNameB, classTime)
    return notFound

def formatPrint(classNameA, classNameB, classTime):
    print(",".join((classNameA, classNameB, classTime)))

def main():
    classDict = {}
    timeDict = {}
    
    noError = True
    
    classAmount = int(input())
    
    for i in range(classAmount):
        currentClass, errorCode = processInput()
        classDict.update(currentClass)
        noError &= errorCode
    
    if not noError:
        print("-1")
        return
    
    classNameArray = list(dict.fromkeys(classDict))
    l = len(classNameArray)
    
    notFound = True
    
    for x in range(l):
        for y in range(x+1, l):
            classNameA = classNameArray[x]
            classNameB = classNameArray[y]
            classA = classDict[classNameA]
            classB = classDict[classNameB]
            notFound &= checkClassTimeError(classNameA, classNameB, classA, classB)
    
    if notFound: print("correct")

if __name__ == '__main__':
    main()
