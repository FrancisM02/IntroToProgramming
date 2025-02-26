# (Game: Learn addition) Write a program that generates two integers under 100 and prompts the user to enter the sum
# of these two integers. The program then reports true if the answer is correct, false otherwise. The program
# is similar to Listing 4.1.

import random

number1 = random.randint(1,99)
number2 = random.randint(1,99)

answer = eval(input(f"What is the sum of {number1} + {number2}:"))

correct_answer = number1 + number2

if answer == correct_answer:
    print("You're Correct!")
else:
    print("You're Incorrect.")