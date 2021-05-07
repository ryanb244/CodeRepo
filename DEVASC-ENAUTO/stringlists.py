
string = input("Input your string:")

stringList = list(string)

reverseString = stringList[::-1]

if stringList == reverseString:
    print("This is a palandrome")
else:
    print("This is not a palandrome")