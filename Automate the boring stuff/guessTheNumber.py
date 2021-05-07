# This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break     # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    




#my program
#guessCount = 1
#while True:
#    if guessCount == 6:
#        print('Sorry you failed')
#        break
#    print('Take a guess.')
#    guess = input()
#    guess = int(guess)
#    if guess == secretNumber:
#        print('Good job! You guessed my number in ' + str(guessCount) + ' guesses!')
#        break
#    
#    elif guess > secretNumber:
#        print('Your guess is too high')
#      
#    elif guess < secretNumber:
#        print('Your guess is too low')
#    guessCount = guessCount + 1
