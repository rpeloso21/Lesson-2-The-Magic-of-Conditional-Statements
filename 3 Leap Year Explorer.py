# Task 1

year = int(input("Please select a year to check:"))


leap = False

if year % 4 == 0 and year % 100 != 0:
    leap = True

elif year % 100 == 0 and year % 400 != 0:
    leap = False

elif year % 4 == 0 and year % 400 == 0:
    leap = True

else:
    leap = False

if leap:
    print("This is a leap year.")

elif not leap:
    print("This is not a leap year.")
