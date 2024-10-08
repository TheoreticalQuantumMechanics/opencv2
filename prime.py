number = int(input("Eneter a number : "))

if (number == 1):
    print(number , "is not a prime number")
elif (number > 1):
    for index in range(2, number):
        # condition
        if (number % index) == 0:
            print(number, " is not a prime number")
            print(index , " times", number//index , " is" , number)
            break
    else:
            print(number, " is a prime number")

else:
    print(number, " is not a prime number")

