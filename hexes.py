"""
	Use turtle graphics to draw a pattern of hexagons
	file: hexes.py
	author: Dylan Lebedin
"""

# imports the turtle module which draws pictures on a canvas window
import turtle


# definitions of functions and procedures


def draw_hexagons():
    """
        Draw a series of hexagons
        :precondition: Turtle is pointing towards the center of the pattern
        :precondition: Turtle's pen is down
        :post-condition: Turtle's state is the same as at start of the function
    """
    turtle.down()
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)


def initialize():
    """
        :post-condition: Turtle's pen is up
        :post-condition: Turtle's pen size is 2.
    """
    turtle.up()
    turtle.pensize(2)


def hexagon_pattern():
    """
        The program creates the first patterns of hexagons that is seen in the hexes-stu.pdf
    """
    draw_hexagons()
    turtle.right(60)
    draw_hexagons()
    turtle.right(60)
    draw_hexagons()
    turtle.right(60)
    draw_hexagons()
    turtle.right(60)
    draw_hexagons()
    turtle.right(60)
    draw_hexagons()


def main():
    """
        The program creates the second pattern of hexagons that is seen in the hexes-stu.pdf
    """
    initialize()
    hexagon_pattern()  # first hexagon pattern
    turtle.left(240)
    hexagon_pattern()  # second hexagon pattern
    print("Click on the close button (X) of the canvas to end the program.")
    turtle.done()
    print("Have a nice day!")


# now call the main function to run the program code

main()
