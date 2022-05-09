# Joshua Francis
# CSC 120
# Midterm Exam 
# 10 / 14 / 2021

# 1. Write a function that takes in two numbers as parameters and returns their remainder. Write comments to explain the code. Use appropriate test cases to run the function.

print (" ")                                     # Spacing
print ("Question 1")                            # Prints Question Number
print (" ")                                     # Spacing

def Remainder(a, b):                            # Function Name and Variables that are being called 
    if (b > 0):                                 # Upper Limit
        print ("The Remainder is" , a%b)        # Prints statement if the above if statememt is true
    elif (b == 0):                              # Invalid Input
        print ("You can not divide by 0!")      # Prints statement if the above elif statememt is true
    elif (a < 0 > b):                           # Lower Limit
        print ("The Remainder is" , a%b)        # Prints statement if the above elif statememt is true

Remainder (20, 5)                               # Positive Integers
Remainder (-15, -13)                            # Negitive Integers 
Remainder (4.5, 2)                              # Positive Decimals
Remainder (-45.75, -20)                         # Negitive Decimals
Remainder (0, 0)                                # Invalid Input, Can not divide by 0
Remainder (5, 0)                                # Invalid Input, Can not divide by 0

# 2. Write a program that uses IF and FOR to print all even numbers from 10 to 50.

print (" ")                                     # Spacing
print ("Question 2")                            # Prints Question Number
print (" ")                                     # Spacing

for c in range (-2897434, 4578634, 2):          # Defines the range and denotes it with variable c 
    if (8 < c < 52):                            # Defines the Upper and Lower Limit
        print (c)                               # Prints statement for the numbers within the Upper and Lower Limit following the defined range 

                                                # Does not require test cases 

# 3. Write a program that uses FOR to print the following pattern. Write comments to explain the code. Note that it is right-aligned. Hint: you can print n blank spaces as print(“ “*n).

print (" ")                                     # Spacing
print ("Question 3")                            # Prints Question Number
print (" ")                                     # Spacing

spaces= " "                                     # Defines spaces as " " in the program
stars = "*"                                     # Defines stars as "*" in the program

for d in range (0, 10, 1):                      # Defines the range and denotes it with variable d, Lines
    for e in range (8, -1, -1):                 # Defines the range and denotes it with variable e
        if (d > 8):                             # Lower Limit for range denoted with variable d
            print(e*spaces + stars * (d - e))   # Prints statement if the above if statement is true

# 4. Write a program that uses FOR to print the following pattern. Write comments to explain the code. Note that it is center-aligned.

print (" ")                                     # Spacing
print ("Question 4")                            # Prints Question Number
print (" ")                                     # Spacing

spaces= " "                                     # Defines spaces as " " in the program
stars = "*"                                     # Defines stars as "*" in the program

for f in range (0, 9, 1):                       # Defines the range and denotes it with variable f, Number of Rows
    for g in range (0, 8-f , 1):                # Defines the range and denotes it with variable g, bases on range f, Number of Spaces
        print (spaces, end = "")                # Prints statement that adds spaces, and makes it on the same line
    for h in range (0, f*2 + 1, 1):             # Defines the range and denotes it with variable h, bases on range f, Number of Columns
        print (stars, end = "")                 # Prints statement that adds stars, and makes it on the same line 
    print ("")                                  # Makes a new line after each row

