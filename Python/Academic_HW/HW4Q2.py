import turtle


def main():     # Main function
    settings()
    sides = int(input("Please enter the num of side you want for the shape: "))
    draw(sides)


def settings():     # Adjust the settings Function
    screen = turtle.Screen()  # Adjust screen size settings
    screen.setup(width=1.0, height=1.0)
    turtle.penup()
    turtle.goto(-150, -250)
    turtle.pendown()

    while True:     # Receive from user the background color and make sure that the user inputs existed color
        try:
            print("Please enter the color you want for background: ", end='')
            turtle.Screen().bgcolor(input())
            break
        except:     # If the color doesn't exist then we asking him again to enter the color
            print("You enter not existed color")

    while True:     # Receive from user the polygon fill color and make sure that the user inputs existed color
        try:
            print("Please enter the fill color you want for the shape: ", end='')
            turtle.fillcolor(input())
            break
        except:
            print("You enter not existed color")

    turtle.speed(int(input("Please enter turtle speed you want (0-10): ")))     # Receive from user turtle speed


def draw(sides):    # Draw the polygon
    turtle.begin_fill()
    for i in range(sides):      # For loop that run sides times of the polygon and draw each interaction one side
        turtle.forward(150 * ((1 / (sides / 10))))      # Adjust the steps by the amount of sides of the polygon(to make sure we can see it fully on the screen)
        turtle.left(180 - ((180*(sides - 2))/sides))    # Move turtle degree by polygon formulation to draw the polygon
    turtle.end_fill()


# Start the program
main()
turtle.done()
