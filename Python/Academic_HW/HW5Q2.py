import turtle


# Turtle Setup
def settings():
    screen = turtle.Screen()    # Adjust screen size settings
    screen.setup(width=1.0, height=1.0)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-300, -300)     # Take turtle to the right starting point
    turtle.pendown()


# Draw The big square
def draw_the_big_square(size):
    turtle.fillcolor("#8A2B0B")
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(size*square_size)
        turtle.left(90)
    turtle.penup()
    turtle.end_fill()
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)
    turtle.right(90)


def draw_the_squares(size, square_size):    # Draw The Squares
    turtle.fillcolor("#E3AF64")
    for row in range(size):    # For loop for size rows
       if row % 2 == 0:    # Turtle draw settings for even rows
            for column in range(size//2):     # Run size//2 times to color the other color board squares in each column
                turtle.begin_fill()
                turtle.forward(square_size)
                turtle.right(90)
                turtle.forward(square_size)
                turtle.right(90)
                turtle.forward(square_size)
                turtle.right(90)
                turtle.forward(square_size)
                turtle.right(90)
                turtle.end_fill()
                if column < ((size//2)-1):  # If we are in the last square then we move to next row, if not move to the next square
                    turtle.forward(square_size * 2)
                else:
                    turtle.left(90)
                    turtle.forward(square_size)
                    turtle.left(90)
       else:   # Odd row settings
            for column in range((size//2)):
                turtle.begin_fill()
                turtle.forward(square_size)
                turtle.left(90)
                turtle.forward(square_size)
                turtle.left(90)
                turtle.forward(square_size)
                turtle.left(90)
                turtle.forward(square_size)
                turtle.left(90)
                turtle.end_fill()
                if column < (size//2 - 1):  # If we are in the last square then we move to next row, if not move to the next square
                     turtle.forward(square_size * 2)
                else:
                     turtle.right(90)
                     turtle.forward(square_size)
                     turtle.right(90)


settings()

size=-1
while size < 0:
    while True:
        try:
            size = int(input("Please insert the size of the screen you want: "))
            break
        except ValueError:
            print("You can enter only integers")

    if(size<0):
        print("Please insert Positive number")

history_choices = open('HistoryChoices.txt', 'a+')
line = history_choices.readline()
while line != "":
    line = history_choices.readline()
history_choices.write(str(size) + '\n')
history_choices.close()

square_size = 70 * (1 / ((int(size / 10)) + 1))
draw_the_big_square(size)
draw_the_squares(size, square_size)

history_choices = open('HistoryChoices.txt', 'r')
print(history_choices.read())
history_choices.close()
turtle.done()