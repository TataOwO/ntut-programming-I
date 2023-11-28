class Player:
    def __init__(self, name, index, money):
        self.name = name
        self.point = 0
        self.index = index
        self.failed = False
        self.money = money
        self.earning = 0
    
    def reset(self):
        self.point = 0
        self.failed = False
    
    def determineContinue(self, inp):
        print(self.name, inp)
        return inp[0] == "Y"
    
    def checkFailed(self):
        if self.point > 10.5:
            self.failed = True
            self.point = 0
            return True
        return False
    
    def doInput(self, scoreTable, playerArray): ## computer not working and im tired of fixing it
        inp = input()
        while self.determineContinue(inp) and not self.failed:
            card = inp.split(" ").pop()
            self.point += scoreTable.get(card, 0)
            self.checkFailed()
            print(self.name, self.point, self.failed)
            inp = input()

    def determineWinning(self, computerPoint):
        return self.point > computerPoint

    def getEarning(self, winningStatus):
        return self.money if winningStatus else -self.money

def earningToString(inp):
    output = str(inp)
    if inp > 0: output = "+" + output
    return output

def main():
    scoreTable = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 0.5,
        "Q": 0.5,
        "K": 0.5
    }
    
    playerCount = int(input())
    moneyArray = [int(x) for x in input().split(" ")]
    firstPick = [scoreTable.get(x) for x in input().split(" ")]
    
    playerArray = []
    for i in range(playerCount):
        playerArray.append(Player(
            "Player{0}".format(i+1),
            i,
            moneyArray[i]
        ))
        playerArray[i].point = firstPick[i]
    
    for each in playerArray:
        each.doInput(scoreTable, playerArray)
    
    computerPoint = firstPick[-1]
    for each in playerArray:
        while computerPoint <= 10.5 and each.point > computerPoint:
            computerPoint += scoreTable.get(input())
    
    for each in playerArray: print(each.__dict__)
    
    if computerPoint > 10.5: computerPoint = 0
    
    computerMoney = 0
    for each in playerArray:
        winningStatus = each.determineWinning(computerPoint)
        earning = each.getEarning(winningStatus)
        each.earning = earningToString(earning)
        computerMoney -= earning
    
    computerEarning = earningToString(computerMoney)
    for each in playerArray:
        print(each.name, each.earning)
    print("Computer", computerEarning)
    

if __name__ == "__main__":
    main()