
"""
*******************************************************************************
Date: 02/14/2023
Programmer: Marco Jacome
Title: Exercise 1.2 - Debugging Practice

Description:
    
Look at the code in the code editor on the right. There are errors in all of the lines 

of code. Fix the code so that it runs without errors.

*******************************************************************************

#Sample code:
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

"""

#solution code:
#1. Missing double quotes before the word Day.
print("Day 1 - String Manipulation")

#2. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')

#3. Extra indentation removed
print('e.g. print("Hello " + "world")')

#4. Extra ( in print function removed.
print("New lines can be created with a backslash and n.")