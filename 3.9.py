#(Financial application: payroll) Write a program that reads the following information and prints a payroll
# statement:
# Employee's name (e.g. Smith)
# Number of hours worked in a week (e.g., 10?)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)

name = str(input("Enter your name: "))
worked_hours = eval(input("Enter worked hours:"))
hourly_pay_rate = eval(input("Enter hourly pay rate:"))
federal_tax = eval(input("Enter rate of federal tax withheld:"))
state_tax = eval(input("Enter rate of state tax withheld:"))

# Formulas for gross and net pay
gross_pay = hourly_pay_rate * worked_hours


# Tax withholding
federal_withholding = gross_pay * federal_tax
state_withholding = gross_pay * state_tax
total_taxes_withheld = federal_withholding + state_withholding
# Pay after taxes taken
net_pay = gross_pay - total_taxes_withheld


print("-Your payroll statement-")
print(f"Name: {name}")
print(f"Total hours worked: {worked_hours}")
print(f"Pay-Rate: {hourly_pay_rate}")
print(f"Gross pay: {gross_pay}")
print("\nDeductions:")
print(f"Federal Tax Withholding rate: {federal_tax * 100} : {federal_withholding}")
print(f"State Tax Withholding rate: {state_tax * 100}: {state_withholding}")
print(f"Total Taxes Withheld: {total_taxes_withheld}")
print(f"Pay After Taxes: {net_pay:.2f}")



