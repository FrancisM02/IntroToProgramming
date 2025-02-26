# (Reverse number) Write a program that prompts the user to enter a four-digit integer and displays the number
# in reverse order.
number = str(input("Enter a 4 digit number:"))

reversed_number = number[::-1]
print("The number reversed is:", reversed_number)
