# Task 1

number1 = int(input("please choose a number:"))
number2 = int(input("pleae choose another number:"))
number3 = int(input("please choose a third number:"))

largest_number = 0
smallest_number = 0

if number1>=number2 and number1>=number3:
    largest_number = number1

elif number2>=number1 and number2>=number3:
    largest_number = number2

elif number3>=number2 and number3>=number1:
    largest_number = number3

print("The largest number is", largest_number)


# Task 2

if number1<=number2 and number1<=number3:
    smallest_number = number1

elif number2<=number1 and number2<=number3:
    smallest_number = number2

elif number3<=number2 and number3<=number1:
    smallest_number = number3

print("The smallest number is", smallest_number)


# Task 3

if number1==number2 and number1==number3:
    print("All the number are the same!")

elif number1 == number2:
    print("Two numbers are the same and they are the first and the second.")

elif number1 == number3:
    print("Two numbers are the same and they are the first and the third.")

elif number2 == number3:
    print("Two numbers are the same and they are the second and third.")



elif number1==number2 and number1==number3:
    print("All the numbers are the same")
