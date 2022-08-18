import turtle

# Turtle Setup
screen = turtle.Screen()    # Adjust screen size settings
screen.setup(width=1.0, height=1.0)
turtle.speed(3)
turtle.showturtle()
turtle.penup()
turtle.goto(-300, -300)     # Take turtle to the right starting point
turtle.pendown()

# Draw The square
turtle.fillcolor("#8A2B0B")
turtle.begin_fill()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.right(90)

# Draw The Squares
turtle.fillcolor("#E3AF64")

for row in range(8):    # For loop for eight rows
    if row % 2 == 0:    # Turtle draw settings for even rows
        for column in range(4):     # Run 4 times to color the other color board squares in each column
            turtle.begin_fill()
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(75)
            turtle.right(90)
            turtle.end_fill()
            if column < 3:  # If we are in the last square then we move to next row, if not move to the next square.
                turtle.forward(150)
            else:
                turtle.left(90)
                turtle.forward(75)
                turtle.left(90)
    else:   # Odd row settings
        for column in range(4):
            turtle.begin_fill()
            turtle.forward(75)
            turtle.left(90)
            turtle.forward(75)
            turtle.left(90)
            turtle.forward(75)
            turtle.left(90)
            turtle.forward(75)
            turtle.left(90)
            turtle.end_fill()
            if column < 3:  # If we are in the last square then we move to next row, if not move to the next square.
                 turtle.forward(150)
            else:
                turtle.right(90)
                turtle.forward(75)
                turtle.right(90)
turtle.done()