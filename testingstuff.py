def singleGame():
    print(format("Yahtzee Score Card"))
    print(format("Upper Section"
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
    print(format("9"),(smallStraight))
    print(format("10"),(largeStraight))
    print(format("11"),(yahtzee))
    print(format("12"),(chance))
    print(format(lowerTotal))

    print("Press the number Correlated to the box you'd like to add a score to.")
    print("")
    holdPrompt.replace(" ", "")
    holdPrompt.lower()
    while holdPrompt != "y" and holdPrompt != "n":
        print("INCORRECT INPUT\n")
        holdPrompt = input("Swap any dice? (y for HITME, n for HOLD): ")
        print("")
        holdPrompt.replace(" ", "")
        holdPrompt.lower()

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
