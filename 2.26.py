# (Turtle: draw a circle) Write a program that prompts the user to enter the center and radius of a circle,
# and then displays the circle and its area, as shown in Figure 2.5
import math
import turtle

x1,y1 = eval(input("Enter the x and y coordinates:"))
radius = eval(input("Enter the radius of circle:"))

# Area formula
area = radius * math.pi ** 2

turtle.penup()
turtle.goto(x1,y1 - radius)
turtle.pendown()
turtle.circle(radius)

# Writes the area inside circle
turtle.penup()
turtle.goto(x1,y1)
turtle.write(f"area = {area:.3f}")
turtle.done()