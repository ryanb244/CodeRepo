

def vol(rad):

    return (4/3)*3.14*(rad**3)


#print(vol(2))

def ran_check(num,low,high):
    if num in range(low, high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is NOT in the range between {low} and {high}')



#ran_check(2,2,7)

def ran_bool(num,low,high):
    if num in range(low, high+1):
        return True
    else:
        return False

#print(ran_bool(3,1,10))

def up_low(s):
    upper = 0
    lower = 0

    for x in s:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
    print(f'No. of Upper case characters : {upper}')
    print(f'No. of Lower case characters {lower}')



#up_low('HELLO Mr. Rogers, how are you this fine Tuesday?')



def multiply(numbers):

    total = 1 

    for i in numbers:
        total *= i

    return total

#print(multiply([1, 2, 3, 1, 1, 1, 1]))