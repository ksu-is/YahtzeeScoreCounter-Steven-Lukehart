def singleGame():
    print(format("Yahtzee Score Card"))
    print(format("Upper Section"
    print(format(aces))
    print(format(twos))
    print(format(threes))
    print(format(fours))
    print(format(fives))
    print(format(sixes))
    print(format(upperTotal))
    print(format(upperBonus))
    print("")
    print(format("Lower Section"))
    print(format(threeOfKind))
    print(format(fourOfKind))
    print(format(smallStraight))
    print(format(largeStraight))
    print(format(yahtzee))
    print(format(chance))
    print(format(lowerTotal))

    holdPrompt = input("Swap any dice? (y for HITME, n for HOLD): ")
    print("")
    holdPrompt.replace(" ", "")
    holdPrompt.lower()
    while holdPrompt != "y" and holdPrompt != "n":
        print("INCORRECT INPUT\n")
        holdPrompt = input("Swap any dice? (y for HITME, n for HOLD): ")
        print("")
        holdPrompt.replace(" ", "")
        holdPrompt.lower()

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
    game = list(game)
    for x in game:
        if x == True:
            statIndex = game.index(x)
    if statIndex == 0:
        yahtzee += 1
    elif statIndex == 1:
        fullHouse += 1
    elif statIndex == 2:
        smallStraight += 1
    elif statIndex == 3:
        largeStraight += 1
    elif statIndex == 4:
        fourOfKind += 1
    elif statIndex == 5:
        threeOfKind += 1
    else:
        pass
    print("")
    gameCount = 1
    print("END OF GAME", gameCount)
    print("-" * 80)
    print("")
