"""
*******************************************************************************
Date: 02/20/2023
Programmer: Marco Jacome
Title: Exercise 3.5 - Love Calculator

Description:
    
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the 

word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.


For Love Scores less than 10 or greater than 90, the message should be:
-----------------------------------------------------------------------

"Your score is **x**, you go together like coke and mentos."


For Love Scores between 40 and 50, the message should be:
-----------------------------------------------------------

"Your score is **y**, you are alright together."


Otherwise, the message will just be their score. e.g.:
-------------------------------------------------------

"Your score is **z**."

*******************************************************************************
"""


print("\nWelcome to the Love Score Calculator!/n")
name1 = input("Enter name 1: ")
name2 = input ("Enter name 2: ")

#Make all names lower case 
name1 = name1.lower()
name2 = name2.lower()

# Combine both names into one string by concatenating strings of name1 and name2
name_all = name1 + name2


#use count() to search name_all for characters in true love

t = name_all.count("t")
r = name_all.count("r")
u = name_all.count("u")
e = name_all.count("e")
 
#add up count of each letter for 'TRUE'
true =  t+r+u+e 
 
l = name_all.count("l")
o = name_all.count("o")
v = name_all.count("v")
e = name_all.count("e")

#add up count of each letter for 'LOVE'
love = l+o+v+e

#convert integers to strings, then concatenate strings together
lovescore_str = str(true) +  str(love) # as string
lovescore = int(lovescore_str)  # as integer

#Display strings as the love score based on love score condition or range
if lovescore <=10 | lovescore >= 90:
    print(f"\nYour score is {lovescore_str}, you go together like coke and mentos.")

elif  lovescore >= 40 & lovescore <= 50:
    print(f"\nYour score is {lovescore_str}, you are alright together.")

else: 
    print("\nYour love score is " + lovescore_str )












