# Alexis McCarroll
# 11/8/2024
# P4LAB1
# Use turtle and loops to draw a square and a triangle

#Import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(3)
pen.pencolor("green")
pen.shape("arrow")

#Code to draw the shapes
for side in range (4):
    pen.forward(100)
    pen.left(90)

#While loops that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1


#wait for user to close window
win.mainloop()
