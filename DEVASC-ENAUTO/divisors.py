
number = int(input("Enter your number:"))
divisors = []

for i in range(number):
    if i != 0:
        if number % i == 0:
            divisors.append(i)
    
    
print(divisors)

