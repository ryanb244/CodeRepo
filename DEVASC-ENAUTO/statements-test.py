
"""print only words that start with 's'

st = 'Print only the words that start with s in this sentenence'

words = st.split()

for i in words:
    if i[0] == 's':
        print(i)

"""

"""Use range() to print all the even numbers from 0 to 10

for i in range(0,11):
    if i % 2 == 0:
        print(i) 

"""




"""Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

numberList = []

for i in range(1,51):
    if i % 3 == 0:
        numberList.append(i)

print(numberList)

"""


"""Go through the string below and if the length of the word is even print 'even!'

st = 'Print every word in this sentence that has an even number of letters'

wordList = st.split()

for i in wordList:
    wordLength = 0
    for j in i:
        wordLength += 1
    if wordLength % 2 == 0:
        print(i)
        
"""



""" Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
"""

"""Use List Comprehension to create a list of the first letters of every word in the string below: """

st = 'Create a list of the first letters of every word in this string'

wordList = st.split()

first = []

for i in wordList:
    first.append(i[0])

print(first)