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
        if box == "1":
            print(format("Please enter how many 1's you rolled this turn"))
            aces = int(input('Enter 1s rolled here: '))
        if box == "2":
            print(format("Please enter how many 2's you rolled this turn"))
            num = int(input('Enter 2s rolled here: '))
            twos = num * 2
        if box == "3":
            print(format("Please enter how many 3's you rolled this turn"))
            num = int(input('Enter 3s rolled here: '))
            threes = num * 3
        if box == "4":
            print(format("Please enter how many 4's you rolled this turn"))
            num = int(input('Enter 4s rolled here: '))
            fours = num * 4
        if box == "5":
            print(format("Please enter how many 5's you rolled this turn"))
            num = int(input('Enter 5s rolled here: '))
            fives = num * 5
        if box == "6":
            print(format("Please enter how many 6's you rolled this turn"))
            num = int(input('Enter 6s rolled here: '))
            sixes = num * 6
        if box == "7":
            print(format("Please enter the all five dice roles"))
            num1=int(input('Enter the first number: '))
            num2=int(input('Enter the second number: '))
            num3=int(input('Enter the thrid number: '))
            num4=int(input('Enter the fourth number: '))
            num5=int(input('Enter the fifth number: '))
            sum=num1+num2+num3+num4+num5
            threeOfKind = sum
        if box == "8":
            print(format("Please enter the all five dice roles"))
            num1=int(input('Enter the first number: '))
            num2=int(input('Enter the second number: '))
            num3=int(input('Enter the thrid number: '))
            num4=int(input('Enter the fourth number: '))
            num5=int(input('Enter the fifth number: '))
            sum=num1+num2+num3+num4+num5
            fourOfKind = sum
        if box == "9":
            input("Press Enter to check off full house.")
            fullHouse = 25
        if box == "10":
            input("Press Enter to check off small straight.")
            smallStraight = 30
        if box == "11":
            input("Press Enter to check off large straight.")
            largeStraight = 40
        if box == "12":
            input("Press Enter to check off Yahtzee!")
            yahtzee = 50
        if box == "13":
            print(format("Please enter the all five dice roles"))
            num1=int(input('Enter the first number: '))
            num2=int(input('Enter the second number: '))
            num3=int(input('Enter the thrid number: '))
            num4=int(input('Enter the fourth number: '))
            num5=int(input('Enter the fifth number: '))
            sum=num1+num2+num3+num4+num5
            chance = sum
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
        totalScore = upperTotal + lowerTotal + upperBonus
        print(format(upperTotal),(" + ")(upperBonus),(" + "),(lowerTotal),(" = "),(totalScore))
        print("")
        print(format("Game Over!!!"))

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
