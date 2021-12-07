def singleGame():
    aces = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    upperTotal = 0
    lowerTotal = 0
    upperBonus = 0
    yahtzee = 0
    fullHouse = 0
    smallStraight = 0
    largeStraight = 0
    fourOfKind = 0
    threeOfKind = 0
    chance = 0
    totalScore = 0
    turnCount = 1
    #turnCount <=13 is a full game
    while turnCount <= 13:
        print("")
        print("")
        print(format("Yahtzee Score Card"))
        print(format("Upper Section"))
        print(format("(1) - ACES = "),(aces))
        print(format("(2) - TWOS = "),(twos))
        print(format("(3) - THREES = "),(threes))
        print(format("(4) - FOURS = "),(fours))
        print(format("(5) - FIVES = "),(fives))
        print(format("(6) - SIXES = "),(sixes))
        print(format("upperTotal = "),(upperTotal))
        print(format("upperBonus = "),(upperTotal),("/"),("63"))
        print("")
        print(format("Lower Section"))
        print(format("(7) - Three of a Kind = "),(threeOfKind))
        print(format("(8) - Four of a Kind = "),(fourOfKind))
        print(format("(9) - Full House = "),(fullHouse))
        print(format("(10) - Small Straight = "),(smallStraight))
        print(format("(11) - Large Straight = "),(largeStraight))
        print(format("(12) - Yahtzee = "),(yahtzee))
        print(format("(13) - Chance = "),(chance))
        print(format("lowerTotal = "),(lowerTotal))
        print("")
        print("")

        print(format("Press the number correlated to the box you'd like to add a score to."))
        box = input('Enter number here: ')
        #aces
        if box == "1":
            print(format("Please enter how many 1's you rolled this turn."))
            aces = int(input('Enter 1s rolled here: '))
            input("Press Enter to continue")
        #twos
        if box == "2":
            print(format("Please enter how many 2's you rolled this turn."))
            num = int(input('Enter 2s rolled here: '))
            twos = num * 2
            input("Press Enter to continue")
        #threes
        if box == "3":
            print(format("Please enter how many 3's you rolled this turn."))
            num = int(input('Enter 3s rolled here: '))
            threes = num * 3
            input("Press Enter to continue")
        #fours
        if box == "4":
            print(format("Please enter how many 4's you rolled this turn."))
            num = int(input('Enter 4s rolled here: '))
            fours = num * 4
            input("Press Enter to continue")
        #fives
        if box == "5":
            print(format("Please enter how many 5's you rolled this turn."))
            num = int(input('Enter 5s rolled here: '))
            fives = num * 5
            input("Press Enter to continue")
        #sixes
        if box == "6":
            print(format("Please enter how many 6's you rolled this turn."))
            num = int(input('Enter 6s rolled here: '))
            sixes = num * 6
            input("Press Enter to continue")
        #three of a kind
        if box == "7":
            yesNoPrompt = input("Did you score a Three of a Kind? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                print(format("Please enter the all five dice roles."))
                num1=int(input('Enter the first number: '))
                num2=int(input('Enter the second number: '))
                num3=int(input('Enter the thrid number: '))
                num4=int(input('Enter the fourth number: '))
                num5=int(input('Enter the fifth number: '))
                sum=num1+num2+num3+num4+num5
                threeOfKind = sum
                input("Press Enter to continue")
            if yesNoPrompt == "n":
                print(format("You scored a 0 in Three of a Kind."))
                threeOfKind = 0
                input("Press Enter to continue")
        #four of a kind
        if box == "8":
            yesNoPrompt = input("Did you score a Four of a Kind? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                print(format("Please enter the all five dice roles."))
                num1=int(input('Enter the first number: '))
                num2=int(input('Enter the second number: '))
                num3=int(input('Enter the thrid number: '))
                num4=int(input('Enter the fourth number: '))
                num5=int(input('Enter the fifth number: '))
                sum=num1+num2+num3+num4+num5
                fourOfKind = sum
                input("Press Enter to continue")
            if yesNoPrompt == "n":
                print(format("You scored a 0 in Four of a Kind."))
                fourOfKind = 0
                input("Press Enter to continue")
        #full house
        if box == "9":
            yesNoPrompt = input("Did you score a Full House? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                input("Press Enter to check off Full House.")
                fullHouse = 25
            if yesNoPrompt == "n":
                input("You scored a 0 in Full House. Press Enter to continue.")
                fullHouse = 0
        #small straight
        if box == "10":
            yesNoPrompt = input("Did you score a Small Straight? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                input("Press Enter to check off Small Straight.")
                smallStraight = 30
            if yesNoPrompt == "n":
                input("You scored a 0 in Small Straight. Press Enter to continue.")
                smallStraight = 0
        #large straight
        if box == "11":
            yesNoPrompt = input("Did you score a Large Straight? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                input("Press Enter to check off Large Straight.")
                largeStraight = 40
            if yesNoPrompt == "n":
                input("You scored a 0 in Large Straight. Press Enter to continue.")
                largeStraight = 0
            #yahtzee
        if box == "12":
            yesNoPrompt = input("Did you score a Yahtzee? (y for yes, n for no): ")
            yesNoPrompt.strip()
            yesNoPrompt.lower()
            if yesNoPrompt == "y":
                input("Press Enter to check off Yahtzee!")
                yahtzee = 50
            if yesNoPrompt == "n":
                input("You scored a 0 in Yahtzee. Press Enter to continue.")
                yahtzee = 0
        #chance
        if box == "13":
            print(format("Please enter the all five dice roles"))
            num1=int(input('Enter the first number: '))
            num2=int(input('Enter the second number: '))
            num3=int(input('Enter the thrid number: '))
            num4=int(input('Enter the fourth number: '))
            num5=int(input('Enter the fifth number: '))
            sum=num1+num2+num3+num4+num5
            chance = sum
            input("Press Enter to continue")
        turnCount = turnCount + 1
        upperTotal = aces + twos + threes + fours + fives + sixes
        lowerTotal = threeOfKind + fourOfKind + chance + yahtzee + smallStraight + largeStraight
        if upperTotal > 63:
            upperBonus = 35
    else:
        print("")
        print("")
        print(format("Yahtzee Score Card"))
        print(format("Upper Section"))
        print(format("ACES = "),(aces))
        print(format("TWOS = "),(twos))
        print(format("THREES = "),(threes))
        print(format("FOURS = "),(fours))
        print(format("FIVES = "),(fives))
        print(format("SIXES = "),(sixes))
        print(format("upperTotal = "),(upperTotal))
        print(format("upperBonus = "),(upperTotal),("/"),("63"))
        print("")
        print(format("Lower Section"))
        print(format("Three of a Kind = "),(threeOfKind))
        print(format("Four of a Kind = "),(fourOfKind))
        print(format("Full House = "),(fullHouse))
        print(format("Small Straight = "),(smallStraight))
        print(format("Large Straight = "),(largeStraight))
        print(format("Yahtzee = "),(yahtzee))
        print(format("Chance = "),(chance))
        print(format("lowerTotal = "),(lowerTotal))
        print("")
        print("")
        totalScore = upperTotal + lowerTotal + upperBonus
        print(format("Upper Total: "),(upperTotal),(" + "),("Upper Bonus: "),(upperBonus),(" + "),("Lower Total: "),(lowerTotal),(" = "),(totalScore))
        print("")
        print(format("Game Over!!!"))
        gamesPrompt = input("Play another game? (y for yes, n for no): ")
        gamesPrompt.strip()
        gamesPrompt.lower()
        while gamesPrompt != "y" and gamesPrompt != "n":
            print("")
            print("INCORRECT INPUT")
            print("")
            gamesPrompt = input("Play another game? (y for yes, n for no): ")
            gamesPrompt.strip()
            gamesPrompt.lower()
        print("")

        if gamesPrompt == "y":
            game = singleGame()
        if gamesPrompt == "n":
            print("Have a nice Day!")
        exit()

def main():
    print("")
    print("-" * 80)
    print("")
    print(format("Welcome to the Yahtzee Score Card!", '61s'), "Written by Steven Lukehart")
    print("")
    print("-" * 80)
    print("")
    print(format("Please enter Player 1's Name."))
    name = input('Enter your name: ')
    print(name)
    print(format("Game 1", '>43s'))
    print("")
    input("Press Enter to continue")
    game = singleGame()

main()
