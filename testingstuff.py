def singleGame():
    print(format("Yahtzee Score Card"))
    print(format("Upper Section"))
    print(format("1"),(aces))
    print(format("2"),(twos))
    print(format("3"),(threes))
    print(format("4"),(fours))
    print(format("5"),(fives))
    print(format("6"),(sixes))
    print(format(upperTotal))
    print(format(upperBonus))
    print("")
    print(format("Lower Section"))
    print(format("7"),(threeOfKind))
    print(format("8"),(fourOfKind))
    print(format("9"),(fullHouse))
    print(format("10"),(smallStraight))
    print(format("11"),(largeStraight))
    print(format("12"),(yahtzee))
    print(format("13"),(chance))
    print(format(lowerTotal))

    print("Press the number Correlated to the box you'd like to add a score to.")
    print("")
    if input = 1
        print(format("Please enter how many 1's you rolled this turn"))
        aces = input('Enter 1s rolled here')
    if input = 2
        print(format("Please enter how many 2's you rolled this turn"))
        num = input('Enter 2s rolled here')
        twos = num * 2
    if input = 3
        print(format("Please enter how many 3's you rolled this turn"))
        num = input('Enter 3s rolled here')
        threes = num * 3
    if input = 4
        print(format("Please enter how many 4's you rolled this turn"))
        num = input('Enter 4s rolled here')
        fours = num * 4
    if input = 5
        print(format("Please enter how many 5's you rolled this turn"))
        num = input('Enter 5s rolled here')
        fives = num * 5
    if input = 6
        print(format("Please enter how many 6's you rolled this turn"))
        num = input('Enter 6s rolled here')
        sixes = num * 6
    if input = 7
        print(format("Please enter the all five dice roles"))
        num1=int(input('Enter the first number: '))
        num2=int(input('Enter the second number: '))
        num3=int(input('Enter the thrid number: '))
        num4=int(input('Enter the fourth number: '))
        num5=int(input('Enter the fifth number: '))
        sum=num1+num2+num3+num4+num5
        threeOfKind = sum
    if input = 8
        print(format("Please enter the all five dice roles"))
        num1=int(input('Enter the first number: '))
        num2=int(input('Enter the second number: '))
        num3=int(input('Enter the thrid number: '))
        num4=int(input('Enter the fourth number: '))
        num5=int(input('Enter the fifth number: '))
        sum=num1+num2+num3+num4+num5
        fourOfKind = sum
    if input = 9
        input("Press Enter to check off full house.")
        fullHouse = 25
    if input = 10
        input("Press Enter to check off small straight.")
        smallStraight = 30
    if input = 11
        input("Press Enter to check off large straight.")
        largeStraight = 40
    if input = 12
        input("Press Enter to check off Yahtzee!")
        yahtzee = 50
    if input = 13
        print(format("Please enter the all five dice roles"))
        num1=int(input('Enter the first number: '))
        num2=int(input('Enter the second number: '))
        num3=int(input('Enter the thrid number: '))
        num4=int(input('Enter the fourth number: '))
        num5=int(input('Enter the fifth number: '))
        sum=num1+num2+num3+num4+num5
        chance = sum

def upperTotal():
    upperTotal = aces + twos + threes + fours + fives + sixes

def upperBonus():
    upperTotal > 63

def main():
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
    print(format("Please Press the number corresponding to the box you would like to add to."))
    if input = 1
        print(format("Please enter how many 1's you rolled this turn"))
        aces = input('Enter 1s rolled here')
    if input = 2
        print(format("Please enter how many 2's you rolled this turn"))
        twos = input('Enter 2s rolled here')

main()
