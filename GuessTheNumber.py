## L'opérateur import  est une fonctions déja écrite . Il est un module qui permet d'importer une autre fonction (module). Ici on appele (random)
import random

##Cette variable indiquera le nombre d'essaie que nous effectuerons.
essai = 0 

print('Bonjour ! Comment t\'appelles-tu ? ')
myName = input()
print('Bonjour, ' + myName + ' Je pense à un nombre entre 1 et 20 et tu dois me trouver la bonne réponse pour passer le mur')


number = random.randint(1,20)
for essai in range(6):
    print('Essaie de le deviner ')
    guess = input()
    guess = int(guess)

    if guess < number :
        print('Trop petit')

    if guess > number:
        print('Trop Grand')

    if guess == number:
        break

if guess == number:
    essai = str(essai + 1)
    print('Bravo ' + myName + ' tu as trouvé mon nombre en ' + essai + ' essais.')

if guess != number:
    number = str(number)
    print('Raté ! le nombre auquel je pensais était ' + number + '.')
