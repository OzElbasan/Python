import random
import time

def displayIntro():
    print(''' Tu est dans la région du mordor. Devant toi se trouve deux grottes.
L'un renferme un dragon cracheur de feu, et l'autre un  dragon te permettant d'atteindre la montagne du destin''')
    print()

def chooseCave():
    cave=''
    while cave != '1' and cave !='2':
        print('Dans quelle grotte vas-tu entrer ? La 1 ou la 2 ?')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Tu t\'approche de la grotte...')
    time.sleep(2)
    print('Tout est sombre et effrayant...')
    time.sleep(2)
    print('un énorme dragon saute devant toi ! ' + 'il ouvre grand ses mâchoires et...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    
    if chosenCave == str(friendlyCave):
        print('te donne son trésor')
    else:
        print('te brûle avec son feu')
    print()
        
playAgain = 'oui'
    
while playAgain == 'oui' or playAgain == 'o':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Veux-tu rejouer ? (oui ou non)')
    playAgain = input()


