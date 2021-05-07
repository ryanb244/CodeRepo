import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] +  '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def Winner(player): 
    if player == 'X':
        #testForWinnerX
        #row
        if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
            return True
            
        elif theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
            return True
        elif theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
            return True
        #column
        elif theBoard['low-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['top-L'] == 'X':
            return True
        elif theBoard['low-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-M'] == 'X':
            return True
        elif theBoard['low-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['top-R'] == 'X':
            return True
        #diagonal
        elif theBoard['low-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-R'] == 'X':
            return True
        elif theBoard['low-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-L'] == 'X':
            return True
        else:
            return False
        
    elif player == '0':
        #testForWinner0
        #row
        if theBoard['top-L'] == '0' and theBoard['top-M'] == '0' and theBoard['top-R'] == '0':
            return True
        elif theBoard['mid-L'] == '0' and theBoard['mid-M'] == '0' and theBoard['mid-R'] == '0':
            return True
        elif theBoard['low-L'] == '0' and theBoard['low-M'] == '0' and theBoard['low-R'] == '0':
            return True
        #column
        elif theBoard['low-L'] == '0' and theBoard['mid-L'] == '0' and theBoard['top-L'] == '0':
            return True
        elif theBoard['low-M'] == '0' and theBoard['mid-M'] == '0' and theBoard['top-M'] == '0':
           return True
        elif theBoard['low-R'] == '0' and theBoard['mid-R'] == '0' and theBoard['top-R'] == '0':
            return True
        #diagonal
        elif theBoard['low-L'] == '0' and theBoard['mid-M'] == '0' and theBoard['top-R'] == '0':
            return True
        elif theBoard['low-R'] == '0' and theBoard['mid-M'] == '0' and theBoard['top-L'] == '0':
            return True
        else:
            return False
    
    
   

    



num = random.randint(0,1)
if num == 1:
    turn = 'X'
else:
    turn = '0'

for i in range(9):
    printBoard(theBoard)
    print('Enter your space in this format: row is low/mid/top. Column is -L/M/R')
    print('Turn for ' + turn + '. Move on which space?')
    while True:
        move = input()
        if move in theBoard:
            if theBoard[move] != ' ':
                print('That space is already taken fuck face, try again')
            else:
                theBoard[move] = turn
                break
        else:
            print('That is not a valid space you fuck, try again')

    #testForWinner
    if Winner('X') == True:
        print('Player X has won!')
        break
    elif Winner('0') == True:
        print('Player 0 has won!')
        break
   
    
    #changeTurns
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    
if Winner('X') == False and Winner('0') == False:
    print('The game is a tie! Like OMFG!')
    
printBoard(theBoard)

    
