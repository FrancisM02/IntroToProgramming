# (Health application: BMI) Revise Listing 4.6, ComputeBMI.py, to let users enter
# their weight in pounds and their height in feet and inches. For example, if a person
# is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches

weight = eval(input("Enter weight in pounds:"))
feet = eval(input("Enter height in feet:"))
inches = eval(input("Enter height inches:"))

# The formula for bmi is = weight(kg) / height(meters) so we have to convert
calc_inches = (feet * 12) + inches
height_m = calc_inches  * 0.0254

weight_kilograms = weight * 0.453592

bmi = weight_kilograms / (height_m ** 2)

print(f"BMI: {bmi:.2}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
elif bmi > 30:
    print("Obesity")



