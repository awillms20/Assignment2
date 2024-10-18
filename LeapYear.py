# Task1: Leap Year Checker
year=int(input("Enter a Year"))
remainder= year % 4
if  not remainder:
    print("This is a leap year") 
else:
    print("This is not a leap year",remainder)


