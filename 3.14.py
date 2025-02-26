# (Turtle: draw the Olympic symbol) Write a program that prompts the user to enter the radius of the rings and draws
# an Olympic symbol of five rings of the same size with the colors blue, black, red, yellow, and green, as shown
# in Figure 3.5c
import turtle

radius = eval(input("Enter the radius of the Olympic rings: "))

turtle.speed(3)
turtle.pensize(6)
turtle.penup()
turtle.goto(-2.2 * radius, 0 - radius)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(radius)

turtle.penup()
turtle.goto(0,0 - radius)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(radius)

turtle.penup()
turtle.goto(2.2 * radius, 0 - radius)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(radius)

turtle.penup()
turtle.goto(-1.1 * radius, -radius - radius)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(radius)

turtle.penup()
turtle.goto(1.1 * radius, -radius - radius)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(radius)

turtle.done()