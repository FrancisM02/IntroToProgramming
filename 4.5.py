# (Find future dates) Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display the future day of the week.

today = eval(input("Enter today's date using integers 0-6,Sunday is 0 and Saturday is 6:"))

added_days = eval(input("Enter a number which will be added to today's number:"))

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
future_days = (today + added_days) % 7

print(f"Today's date is {days_of_week[today]} and the future day of the week will be {days_of_week[future_days]}")

