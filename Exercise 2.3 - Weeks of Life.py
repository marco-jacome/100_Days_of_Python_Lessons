"""
*******************************************************************************
Date: 02/15/2023
Programmer: Marco Jacome
Title: Exercise 3 - Weeks in Life

Description:

Create a program using maths and f-Strings that tells us how many days, weeks, 

months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time 

left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the 

positions of the commas and full stops.
*******************************************************************************
"""
# declarations
max_age = 90

# Get user age
usr_age = input("What is your current age? ")

# Convert to input from string to integer
age = int(usr_age)

# Calculate how many years remaining until max age
years_of_life = max_age - age

# determine the number of days, weeks, and months of life for user
months_of_life = years_of_life * 12
weeks_of_life = years_of_life * 52
days_of_life = years_of_life * 365

# Print results 
print(f"You have {days_of_life} days, {weeks_of_life} weeks, and {months_of_life} months left in your life!")