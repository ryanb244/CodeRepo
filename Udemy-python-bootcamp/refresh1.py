

while True:
    print('Player 1 enter:')
    player1 = input()
    print('Player 2 enter:')
    player2 = input()
    
    if player1 == 'rock' and player2 == 'scissors':
        print('player1 wins')
    elif player1 == 'rock' and player2 == 'paper':
        print('player2 wins')
    elif player1 == 'scissors' and player2 == 'rock':
        print('player2 wins')
    elif player1 == 'scissors' and player2 == 'paper':
        print('player 1 wins')
    elif player1 == 'paper' and player2 == 'scissors':
        print('player2 wins')
    elif player1 == 'paper' and player2 == 'rock':
        print('player1 wins')
    elif player1 == player2:
        print('tie! Play again')
        
