# Financial application: calculate tips.) Write a program that reads the subtotal and the gratuity rate
# and computes the gratuity and total. For example, if the user enters "10" for the subtotal and "15%" for the
# gratuity rate, the program displays "1.5" as the gratuity and "11.5" as the total.

subtotal = eval(input("Enter the subtotal:"))
rate_of_gratuity = eval(input("Enter the gratuity rate:"))

gratuity = (rate_of_gratuity / 100) * subtotal
total = subtotal + gratuity

print(f"The gratuity is {gratuity} and the total {total}")

