"""
*******************************************************************************
Date: 02/14/2023
Programmer: Marco Jacome
Title: Exercise 1.4 - Variables

Description:

Write a program that switches the values stored in the variables a and b.

*******************************************************************************
"""

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
temp = a
a = b
b = temp
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)