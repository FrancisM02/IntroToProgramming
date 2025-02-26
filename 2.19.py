# (Financial application: calculate future investment value) Write a program that reads in an investment amount,
# the annual interest rate, and the number of years, and displays the future investment value using the
# following formula:
# futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^monthlyInterestRate/

investment = eval(input("Enter your investment:"))
annual_interest_rate = eval(input("Enter the annual interest rate of investment:"))
years = eval(input("Enter the amount of years:"))
# Monthly Rate
monthly = (annual_interest_rate / 100) / 12
months = 12 * years

future_investment = investment * (1 + monthly) ** months

print(f"The investment in the future will be {future_investment:.3f}")