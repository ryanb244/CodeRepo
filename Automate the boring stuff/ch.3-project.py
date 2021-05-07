def collatz(number):
    if (number%2) == 0:
        print(number//2)
        return (number//2)
    elif (number%2) == 1:
        print(3*number+1)
        return (3*number+1)

while True:
    try:
        print('Enter Number bitch:')
        numberEntered = int(input())
        break
    except ValueError:
        print('Mother fucker I said a number')

while numberEntered != 1:
        numberEntered = collatz(numberEntered)
    
    
