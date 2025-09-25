#******CONTROL STATEMENTS*****************
# Control statements are used to control the flow of execution in a program.
# They help you decide what to execute, how many times, and when to skip or stop certain parts of code.
# Conditional statements >>(if,elif,else)
# if – checks the first condition

# elif – checks more conditions if previous ones are false

# else – runs when no conditions are true

# a program to check whether a person is adult or not
age = 18

if age >= 18:
    print("You are an adult.")  # Runs if condition is True
else:
    print("You are a minor.")   # Runs if condition is False

# find greatest among the numbers enter by user
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if( a>b and a>c and a>d):
    print(f"greter number is {a}")

elif(b>a and b>c and b >d):
    print(f"Gretest number is {b}")

elif(c>a and c>b and c>d):
    print(f"Greatest number is {c}")

else:
    print(f"Greatest number is {d}")    
