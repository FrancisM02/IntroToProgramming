# (Population projection) The US Census Bureau projects population based on the following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years.
# Assume the current population is 312032486 and one year has 365 days. Hint: in Python, you can use integer
# division operator // to perform division. The result is an integer. For example, 5 // 4 is 1 (not 1.25) and
# 10 // 4 is 2 (not 2.5)

#Projections
currentPopulation = 312032486
seconds_in_Year = 365 * 24 * 60 * 60

birth_rate = 7 # A birth every 7 seconds
death_rate = 13 # Death every 13 seconds
immigrant_rate = 45 #Immigrant enters the country every 45 seconds

calc_birth_rate = seconds_in_Year // 7
calc_death_rate = seconds_in_Year // 13
calc_immigrant_rate = seconds_in_Year // 45

yearly_change = calc_birth_rate + calc_immigrant_rate - calc_death_rate


print("The Yearly Population Projection for the next 5 years")
year1 = currentPopulation + yearly_change
print(f"Year1: {year1}")
year2 = year1 + yearly_change
print(f"Year1: {year2}")
year3 = year2 + yearly_change
print(f"Year1: {year3}")
year4 = year3 + yearly_change
print(f"Year1: {year4}")
year5 = year4 + yearly_change
print(f"Year1: {year5}")









