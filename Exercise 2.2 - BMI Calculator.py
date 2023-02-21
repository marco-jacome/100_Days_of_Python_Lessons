"""
*******************************************************************************
Date: 02/15/2023
Programmer: Marco Jacome
Title: Exercise 2 - BMI Calculator

Description:
    
 Write a program that calculates the Body Mass Index (BMI) from a
 user's weight and height. The BMI is a measure of someone's weight taking 
 into account their height. e.g. If a tall person and a short person both 
 weigh the same amount, the short person is usually more overweight. The BMI 
 is calculated by dividing a person's weight (in kg) by the square of their 
 height (in m):
*******************************************************************************
"""

# 1. Get user height and weight
usr_weight = input("Enter your weight (kg): ")
usr_height = input("Enter your height (m): ")


# 2. Verify data type of user input
print("User input data type verification: ")
print("usr_weight: ", type(usr_height))
print("usr_height: ", type(usr_weight))

# 3. Convert string to float
weight = float(usr_weight)
height = float(usr_height)

# 4. Calculate BMI 
BMI_float  = weight/(height**2)

# 5. Convert BMI to integer
BMI_int = int(BMI_float)

print("Calculated BMI is: ", BMI_int )