# (Sort three integers) Write a program that prompts the user to enter three integers
# and displays them in increasing order.

int1 = eval(input("Enter integer 1:"))
int2 = eval(input("Enter integer 2:"))
int3 = eval(input("Enter integer 3:"))

if int1 > int2:
    int1, int2 = int2, int1
if int2 > int3:
    int2, int3 = int3, int2

print(f"The numbers in increasing order: {int1},{int2},{int3}")