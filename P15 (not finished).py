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

def getMedian(array):
    arrayLength = len(array)
    i = int(arrayLength*0.5)
    if arrayLength % 2:
        return array[i]
    return sum(array[i: i+2]) * 0.5

def getMode(array):
    sa = sorted(list(set(array)))
    sd = {x:array.count(x) for x in sa}
    sv = list(sd.values())
    sk = list(sd.keys())
    
    m = max(sv)
    return sk[sv.index(m)]

def get4r6i(num, digit):
    tempNum = num * (10 ** digit)
    zerothDigit = int(tempNum) % 10 # XXXXXO.X
    firstDigit = int(tempNum*10) % 10 # XXXXXX.O
    
    if firstDigit == 5: tempNum += zerothDigit % 2
    if firstDigit >= 6: tempNum += 1
    
    return int(tempNum) / (10 ** digit)

def calculateBMI(weight, height):
    bmi = weight / (height * height)
    return get4r6i(bmi, 2)

def formatPrint(num):
    print("%.2f" % (num))

def main():
    bmiArray = []
    
    for i in range(int(input())):
        height, weight = [float(x) for x in input().split(" ")]
        bmiArray.append(calculateBMI(weight, height))
    
    bmiArray.sort()
    
    formatPrint(max(bmiArray))
    formatPrint(min(bmiArray))
    formatPrint(getMedian(bmiArray))
    formatPrint(getMode(bmiArray))

if __name__ == '__main__':
    main()
