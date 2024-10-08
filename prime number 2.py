number = int(input("number : "))

for i in range(2, number):
    if (number % i == 0):
            print(number , "it's not prime number")
else:
    print(number , "prime number")
