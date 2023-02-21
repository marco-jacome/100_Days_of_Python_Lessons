"""
Date: 02/15/2023
Programmer: Marco Jacome
Title: Exercise 1 - Data Types

Description: Write a program that adds the digits in a 2 digit number.
             e.g. if the input was 35, then the output should be 3 + 5 = 8

"""

# 1. Get user input 

user_input = input("Please enter a two digit number: " )

# 2. Verify user input data type 
# print(type(user_input)) 



# 3. Retrieve or seperate elements from string by indexing
digit1_str = user_input[0]
digit2_str = user_input[1]

# 4. Verify elements have been indexed correctly 
# print(digit1_str)
# print(digit2_str)


# 5. Convert user input from string to integer
digit1_num = int(digit1_str)
digit2_num = int(digit2_str)

# 6. Store sum in variable
sum_num = digit1_num + digit2_num

# 7. Print sum 
print(sum_num )