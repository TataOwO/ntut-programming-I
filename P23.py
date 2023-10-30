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
    
    playerScore = scoreTable.get(input())
    enemyScore = scoreTable.get(input())
    playerContinueStatus = True
    # i actually wanted to write this with classes and objects,
    # but i figured that would take a lot more time than
    # doing it like this 
    while True:
        # this variable saves whether or not either players has
        # decided to get more cards or not
        hasInput = False
        
        if playerContinueStatus:
            #
            playerContinueStatus = True if input() == "Y" else False
            
            # quits player input if player does not want to continue
            if not playerContinueStatus: continue
            
            # adds player score by the input
            playerScore += scoreTable.get(input())
            hasInput = True
        
        if playerScore > 10.5:
            print("computer win")
            return
        
        if enemyScore <= 8:
            enemyScore += scoreTable.get(input())
            hasInput = True
        if enemyScore > 10.5:
            print("player win")
            return
        
        if hasInput: continue
        
        if playerScore > enemyScore:
            print("player win")
        elif playerScore < enemyScore:
            print("computer win")
        else:
            print("it's a tie")
        return


if __name__ == "__main__":
    main()