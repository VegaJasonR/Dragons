import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see three caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other caves
    are empty or have dragons that are greedy and hungry,
    and will eat you on sight.''')
    print()
    time.sleep(2)

def chooseCave():
    chosenCave = int(input('Choose a cave to enter (1, 2, or 3): '))
    return chosenCave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    
    friendlyCave = random.randint(1, 3)
    emptyCave = random.choice([cave for cave in [1, 2, 3] if cave != friendlyCave])

    if chosenCave == friendlyCave:
        print('A friendly dragon appears and gives you his treasure!')
    elif chosenCave == emptyCave:
        print('You chose an empty cave. There is nothing here.')
        print('Choose another cave to explore.')
        chosenCave = chooseCave()
        checkCave(chosenCave)
    else:
        print('A dragon gobbles you down in one bite!')

playAgain = 'yes'
while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()