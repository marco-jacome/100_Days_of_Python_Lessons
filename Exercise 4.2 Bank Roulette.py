"""
*******************************************************************************
Date: 2/24/2023
Programmer: Marco Jacome
Title: Exercise 4.2 - Banker Roulette

Description:

You are going to write a program that will select a random name from a list of 

names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function. Line 8 splits the

string names_string into individual names and puts them inside a List called 
 
names. For this to work, you must enter all the names as names followed

by comma then space. e.g. name, name, name
*******************************************************************************
"""

import random

#1. Prompt user to get everybody's name.
names_string = input("Give me everybody's names, separated by a comma. ")
"""NOTE: Using the input function will produce a large string with commas in 
between each name"""

names = names_string.split(", ")
"""NOTE: Using the .split() function on the string will allow the specification
in which character to split the string and to seperate items into a list.
each name will be an item in the list and variable name will store the list 
of names entered from the input."""


#2. Count how many people are on the list.
number_of_names = len(names) - 1  
"""NOTE: Accounting for indexing begins at 0"""

#3. Generate a random number generator based on the number names in list.
random_name =  random.randint(0, number_of_names)

#4. Generated number will determine which person will pay for food bill. 
choose_name = names[random_name]

# 5. Display chosen name and output
print(f"{choose_name} is going to buy the meal today!")

