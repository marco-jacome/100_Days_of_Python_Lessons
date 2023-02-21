"""
*******************************************************************************
Date: 02/16/2023
Programmer: Marco Jacome
Title: Exercise 3.2 - BMI 2.0

Description:
    
Write a program that interprets the Body Mass Index (BMI) based on a user's 

weight and height. It should tell them the interpretation of their BMI based 

on the BMI value.

Under 18.5 they are underweight

Over 18.5 but below 25 they have a normal weight

Over 25 but below 30 they are slightly overweight

Over 30 but below 35 they are obese

Above 35 they are clinically obese.

*******************************************************************************
"""


# 1. Get user height and weight
usr_weight = input("Enter your weight (kg): ")
usr_height = input("Enter your height (m): ")



# 3. Convert string to float
weight = float(usr_weight)
height = float(usr_height)

# 4. Calculate BMI 
BMI  = weight/(height**2)


# 5. Determine BMI range
if BMI < 18.5:
    print(f"Your BMI is {BMI:0.2f}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI:0.2f}, you are at normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI:0.2f}, you are slightly overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI:0.2f}, you are obese")
else:
    print(f"Your BMI is {BMI:0.2f}, you are clinically obese")
    


















