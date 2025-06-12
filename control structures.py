## if statements
'''
Syntax

if condition
   logic
elif condition
   logic
   else:
       logic
'''

## A program that accepts a number from the user(1-9), 

print("welcome to number teller")
number = int(input("please enter a number between 1 and 9"))
if number == 1:
    print("you have entered number one")
elif number == 2:
    print("you have entered number two")
elif number == 3:
    print("you have entered number three")
elif number == 4:
    print("you have entered number four")
elif number == 5:
    print("you have entered number five")
elif number == 6:
    print("you have entered number six")
elif number == 7:
    print("you have entered number seven")
elif number == 8:
    print("you have entered number eight")
elif number == 9:
    print("you have entered number nine")
else:
    print("invalid, please enter a number between 1 and 9")

  ##TO DO

mark = float(input("enter a mark between 0 and 100"))
if 91 >= mark <= 100:
    grade = "A+"
elif 80 >= mark < 90:
    grade = "A"
elif 70 >= mark < 80:
    grade = "B"
elif 60 >= mark < 70:
    grade = "C"
elif 50 >= mark < 60:
    grade = "D"
elif 40 >= mark < 50:
    grade = "E"
elif 0 >= mark < 40:
    grade = "F"
else:
    print("invalid, please enter a mark between 0 and 100")