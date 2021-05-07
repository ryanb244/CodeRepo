def CommaCode(yourList):
    i=0
    yourString = ''
    while True:
        if i == len(yourList) - 1:
            yourString = yourString + 'and ' + yourList[i]
        else:
            yourString = yourString + yourList[i] + ', '
        i += 1
        if i >= len(yourList):
            break
    return yourString
    

myList = ['Cats', 'Dogs', 'Birds', 'Squirrels', 'Alligators']
print(CommaCode(myList))

