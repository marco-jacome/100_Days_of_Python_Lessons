"""
*******************************************************************************
Date: 02/20/2023
Programmer: Marco Jacome
Title: Exercise 3.4 - Pizza Order Practice

Description:
    
Congratulations, you've got a job at Python Pizza. Your first job is to build

an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

*******************************************************************************
"""
# declarations and initialize variables 

bill = 0
small_pizza = 15
medium_pizza  =  20
large_pizza = 25
pepperoni_small = 2
pepperoni_med_lrg = 3
extra_cheese = 1



# Greet User
print("Welcome to Pizza Deliveries!")

#Prompt user for size
print("What size pizza would you like to order?")
usr_size = input("Small, Medium, or Large? : ")
usr_pepperoni = input("Do you want pepperoni?: ")
usr_cheese = input("Do you want extra cheese?: ")

#update bill from size input
if usr_size == "S":
    bill = small_pizza
       
    if usr_pepperoni == "Y":
        bill = bill + pepperoni_small
    
    
    if usr_cheese == "Y":
        bill = bill + extra_cheese
        

elif usr_size == "M":
    bill = medium_pizza
   
    if usr_pepperoni == "Y":
        bill = bill + pepperoni_med_lrg
  
  
    if usr_cheese == "Y":
        bill = bill + extra_cheese
      

else:
    bill = large_pizza
    
    if usr_pepperoni == "Y":
        bill = bill + pepperoni_med_lrg
    
    
    if usr_cheese == "Y":
        bill = bill + extra_cheese
        


#update bill 
print(f"The total is ${bill:0.2f}.")













