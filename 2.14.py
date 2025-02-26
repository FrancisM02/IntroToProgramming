# (Geometry: area of a triangle) Write a program that prompts the user to enter the three points "(x1, y1)"
# "(x2,y2)", and "(x3,y3)" of a triangle and displays its area. The formula for computing the area of a triangle
# is "s = (side1 + side2 + side3) / 2"
import math
print("Enter the 3 points of a Triangle Below")
x1,y1 = eval(input("Enter x1 and y1:"))
x2,y2 = eval(input("Enter x2 and y2:"))
x3,y3 = eval(input("Enter x3 and y3:"))
# The three sides
side1 = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
side2 = math.sqrt((x3-x2) ** 2 + (y3-y2) ** 2)
side3 = math.sqrt((x1-x3) ** 2 + (y1-y3) ** 2)
# Formula/value s
s = (side1 + side2 + side3) / 2
# Area Formula
area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))

print(f"The area of the triangle is {area:.3f}")

