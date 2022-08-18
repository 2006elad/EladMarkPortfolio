import turtle

# Turtle Setup
screen = turtle.Screen()    # Adjust screen size settings
screen.setup(width=1.0, height=1.0)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-300, -300)     # Take turtle to the right starting point
turtle.pendown()

# Draw The square
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.forward(720)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(720)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.penup()
turtle.forward(90)
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.end_fill()

# Draw The circles
turtle.fillcolor("white")

for row in range(6):    # For loop for six rows
    print("Row Number: ", row + 1)  # Print the row num for later use in move's section
    if row % 2 == 0:    # Turtle draw settings for even rows
        for column in range(7):     # Run 7 times for draw the board circles in each column
            print("Column Number: ", column + 1, "\tTurtle X/Y: ", turtle.pos())   # Print the Coordinates of each circle to color them later in move section
            turtle.begin_fill()
            turtle.circle(30)
            turtle.end_fill()
            turtle.penup()
            if column < 6:  # If we are in the last circle then we move to next row, if not move to the next circle.
                turtle.right(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.pendown()
            else:
                turtle.forward(100)
                turtle.pendown()
    else:   # Odd row settings
        x = 7   # Variable for print purposes (In odds the last row is the first row we are printing)
        for column in range(7):
            print("Column Number: ", x, "\tTurtle X/Y: ", turtle.pos())
            x = x - 1   # Adjust x for the next column index print
            turtle.begin_fill()
            turtle.circle(30)
            turtle.end_fill()
            turtle.penup()
            if column < 6:
                turtle.left(90)
                turtle.forward(100)
                turtle.right(90)
                turtle.pendown()
            else:
                turtle.forward(100)
                turtle.pendown()
turtle.penup()

# 10 first move
turtle.speed(5)    # We change the speed so it will look like a real match

# move 1:
turtle.goto(90.00, -250.00)     # We use the data we got on the print and use it to color the desirable circle
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 2:
turtle.goto(-10.00, -250.00)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 3:
turtle.goto(190.00, -250.00)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 4:
turtle.goto(290.00, -250.00)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 5:
turtle.goto(90.00, -150.00)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 6:
turtle.goto(90.00, -50.00)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 7:
turtle.goto(190.00, -150.00)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 8:
turtle.goto(-10.00, -150.00)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 9:
turtle.goto(290.00, -150.00)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move 10:
turtle.goto(-110.00, -250.00)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.done()
