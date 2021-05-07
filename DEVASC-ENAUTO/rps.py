
playAgain = ''

while playAgain != 'no':
    player1 = str(input("Go Player1:")).lower()
    player2 = str(input("Go Player2:")).lower()
    if player1

    if player1 == player2:
        print("It's a tie!")
        playAgain = input("Play again? (yes or no):")
    elif player1 == 'rock' and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper' or player1 == 'paper' and player2 == 'rock':
        print("Player1 wins!")
        playAgain = input("Play again? (yes or no):")
    else:
        print("Player 2 wins!")
        playAgain = input("Play again? (yes or no):")
