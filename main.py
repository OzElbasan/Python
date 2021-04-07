import random
HANGMAN_PICS =['''
    +---+
        |
        |
        |
       === ''', '''
     +---+
     o   |
         |
         |
        === ''', '''
     +---+
     o   |
     |   |
         |
        === ''', '''
     +---+
     o   |
    /|   |
         |
        === ''', '''
     +---+
     o   |
    /|\  |
         |
        === ''', '''
     +---+
     o   |
    /|\  |
    /    |
        === ''', '''
     +---+
     o   |
    /|\  |
    / \  |
        === ''']
        

words = 'aigle singe consitution pays amour visage civilisation chien chat victoire singe continent pause pose ours cochon' \
        'oie tigre lion panthere serpent aigle pigeon singe gorille asticot furet sanglier belier vache chevre poule porc' \
        'motive paresseux sociable bordelique rigoureux autonome equipe solitude affection amour amoureux maladroit ' \
        'continent europe afrique asie amerique antarctique oceanie volcan montagne riviere plaine jungle terrain' \
        'playstation xbox wii zelda warcraft java python sql php javascript html css  '.split()


##Fonction pour que l'ordinateur choississe au hasard un mot dans notre liste
def getRandomWord(wordList):
    ##permet de parcourir notre list en choissisant un mot au hasard
    ##Dans une list, l'index commence à 0
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

##Fonction pour faire affichier le pendu ainsi que les lettres correctes et incorrectes
def displayBoard(missedLetters, correctLetters, secretWords):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Mauvaises lettres :', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_' * len(secretWords)
    ##Remplace les tirets par les lettres correctes
    for i in range(len(secretWords)):
        if secretWords[i] in correctLetters:
            blanks = blanks[:i] + secretWords[i] + blanks[i+1:] ##Parcours du debut à la fin le mot secret et verifie à quel endroit ce trouve la lettre exacte. On ajoute +1 aussi car notre boucle commence à l'index 0 et non 1.
    ##on affiche ici les lettres correctes
    for letter in blanks:
        print(letter, end='')
    print()

def getGuess(alreadyGuessed):
    ##Permet au joueurs d'afficher la lettre saisie. La fonction s'assurera qu'il s'agit d'une unique lettre et de rien d'autre
    while True:
        print('Propose une lettre.')
        guess=input()
        guess=guess.lower()
        ##Vérifier la proposition du joueur
        if len(guess) != 1:
            print('Propose une seul lettre à la fois !')
        elif guess in alreadyGuessed:
            print('Tu as déjà demandé cette lettre.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Propose une lettre de l\'alphabet !')
        else:
            return guess

##Demande au joueur s'il veut rejouer
def playAgain():
    print('Veux-tu rejouer (oui ou non)?')
    return input().lower().startswith('o')

print('P E N D U ')
missedLetters = ''
correctLetters = ''
secretWords = getRandomWord(words)
gameIsDone = False

##Ce boucle nous permet d'appeler la fonction displayBoard() en passant les trois variables pré-configurées et permet de dessiner le pendu en fonction du nombre de lettres fausses ou correctes
while True:
    displayBoard(missedLetters, correctLetters, secretWords)

    ##Inviter le joueur à saisir une lettre
    guess = getGuess(missedLetters + correctLetters)

    ##Vérifier si la lettre est bonne
    if guess in secretWords:
        correctLetters = correctLetters + guess

    ##Verifier si le joueur a gagné
    foundAllLetters = True
    for i in range(len(secretWords)):
        if secretWords[i] not in correctLetters:
            foundAllLetters = False
            break
    if foundAllLetters:
        print('Oui ! Le mot secret est "' + secretWords + ' " ! Tu as gagné !')
        gameIsDone = True
        ##Gérer une mauvaise réponse
    else:
        missedLetters = missedLetters + guess

    ##Vérifier si le joueur à perdu
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWords)
        print('Tu as épuisé tous tes essais ! \nAprès '
              + str(len(missedLetters))
              + 'mauvaises lettres et '
              + str(len(correctLetters))
              + 'lettres exactes, le mot secret était"'
              + secretWords + '".')
        gameIsDone = True

    ##Arrêter yu recommencer le jeu
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone= False
            secretWords = getRandomWord(words)
        else:
            break
