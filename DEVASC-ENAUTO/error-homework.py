
"""

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Sorry you cant do that")

"""


"""
x = 5
y = 0

try:
    z = x/y
except:
    print("LEARN MATH YOU FUCK")
finally:
    print(" :) ")

"""




def ask():
    
    while True:
        try:
            number = int(input("Please enter an int: "))
        except:
            print("Not an int you fuck, try again")
        else:
            print(f"Thank you, your square is: {number**2}")
            break

ask()

        

