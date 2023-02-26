"""
*******************************************************************************
Date: 2/24/2023
Programmer: Marco Jacome
Title: Exercise 4.1 - Name

Description:

You are going to write a virtual coin toss program. It will randomly tell the

 user "Heads" or "Tails".Important, the first letter should be capitalised and

 spelt exactly like in the example e.g. Heads, not heads.There are many ways 
 
 of doing this. But to practice what we learnt in the last lesson, you should

 generate a random number, either 0 or 1. Then use that number to print out 
 
 Heads or Tails. e.g. 1 means Heads 0 means Tails
*******************************************************************************
"""

import random

coin = random.randint(0,1)

if coin == 1:
    print("Heads")
else:
    print("Tails")