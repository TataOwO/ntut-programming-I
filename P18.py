def createTriangle(size, start=1, fillin="*", filler=" "):
    outputArray = []
    for c in range(start, size+1):
        text = ""
        text += fillin*c
        text += filler*(size-c)
        outputArray.append(text)
    return outputArray

def createPyramid(size, fillin="*", filler="#"):
    rSide = createTriangle(size  , 1, fillin, filler)
    lSide = createTriangle(size-1, 0, fillin, filler)
    lSide = ["".join(list(reversed(x))) for x in lSide]
    output = list(zip(lSide, rSide))
    output = ["".join(x) for x in output]
    return output

def createDiamond(size, fillin="*", filler=" "):
    size = int(size/2)
    upSide   = createPyramid(size+1, fillin, filler)
    downSide = createPyramid(size  , fillin, filler)
    downSide = [" "+x+" " for x in downSide]
    
    downSide.reverse()
    output = upSide + downSide
    return output

def createFish(size, fillin="*", filler=" "):
    diamond = createDiamond(size, fillin, filler)
    
    size = int(size/2)
    tail = []
    
    upTail   = createTriangle(size  , 1, "-", filler)
    downTail = createTriangle(size-1, 0, "-", filler)
    downTail.reverse()
    
    upTail   = [    x[::-1] for x in upTail]    
    downTail = [" "+x[::-1] for x in downTail]
    
    tail.append(filler*size)
    tail.extend(upTail)
    tail.extend(downTail)
    tail.append(filler*size)
    
    output = list(zip(diamond, tail))
    output = ["".join(x) for x in output]
    return output

def printFinalProduct(array):
    for each in array: print("".join(each))

def main():
    id = int(input())
    num = int(input())
    if id not in range(1, 5):
        print("error")
        return
    if num not in range(3, 50, 2):
        print("error")
        return
    if id == 1:
        printFinalProduct(createPyramid(num))
    if id == 2:
        printFinalProduct(createPyramid(num)[::-1])
    if id == 3:
        printFinalProduct(createDiamond(num))
    if id == 4:
        printFinalProduct(createFish(num))

if __name__ == "__main__":
    main()
