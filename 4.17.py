# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rock paper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws.
import random
comp_ai = random.randint(0,2)
user = eval(input("Scissors is 0, Rock is 1, and Paper is 2:"))
choices = ["Scissor", "Rock", "Paper"]

print(f"You: {choices[user]}, Comp: {choices[comp_ai]}")

if user == comp_ai:
    print("Draw!")
elif user == 0 and comp_ai == 2:
    print("User wins!, CPU loses")
elif user == 1 and comp_ai == 0:
    print("User wins!, CPU Loses.")
elif user == 2 and comp_ai == 1:
    print("User wins! CPU loses.")
else:
    print("CPU wins!, User loses!")