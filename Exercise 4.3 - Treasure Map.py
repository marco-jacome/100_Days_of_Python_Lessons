"""
*******************************************************************************
Date: 
Programmer: Marco Jacome
Title: Exercise # - Name

Description:
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks 

like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code 

print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square,

 each on a new line. 

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']


Your job is to write a program that allows you to mark a square on the map using a 

two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical 

axis). 

So an input of 23 should place an X at the position shown below:

*******************************************************************************
"""
# Generate Welcome Prompt, and explain user what to do
print("\nWelcome to the Treasure Map Game!\n")
#Initialize map as nested lists with 3 elements in each list
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("\nYou are a pirate who needs to bury his/her treasure somewhere on the map above.")
# Get user input, data type will be a string of two characters
position = input("Where do you want to put the treasure? ")
# Split characters in string to elements in a list
col_str = position[0]
row_str = position[1]
# Convert string characters in list to integers
# Assign left-hand-side integer as column input
# Assign right-hand-side integer as row input 
col_int = int(col_str) - 1 #Elemement index, -1 accounts for index begins at 0.
row_int = int(row_str) - 1 #list index, -1 accounts for index begins at 0.

# Place X at that list location
map[row_int][col_int] = " ⭐"

# Print Map
print(f"{row1}\n{row2}\n{row3}")
 

































