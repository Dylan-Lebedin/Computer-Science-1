"""
Create a function that draws a pattern of zigzags
file: zigzag.py
author: Dylan Lebedin
"""
# import turtle
import turtle

# definitions of functions and procedures


def draw_zigzag(depth, size):
    """
    Draws a series of zigzags
    If depth % 2 == 0 then color is red, else color is green
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function
    """
    depth = int(depth)
    size = int(size)

    if depth == 0:  # base case: if depth < 1, then pass
        pass
    elif depth == 1:  # if depth is equal to one only draw one zigzag
        # depth % 2 == 1, color is green
        turtle.color('green')
        turtle.down()
        turtle.left(90)
        turtle.forward(size/2)
        turtle.right(90)
        turtle.forward(size)
        turtle.backward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(90)
        turtle.back(size/2)
        turtle.left(90)
    else:  # if depth is more than one use recursion to draw the other zigzags
        # If depth % 2 == 0 then color is red, else color is green
        if depth % 2 == 0:
            turtle.color('red')
        else:
            turtle.color('green')
        turtle.down()
        turtle.left(90)
        turtle.forward(size/2)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(45)
        # recursively calls function when turtle reaches end of top part of zigzag
        draw_zigzag(depth - 1, size/2)
        turtle.right(45)
        # Check to see if depth % 2 == 0 when turtle goes over the line again
        if depth % 2 == 0:
            turtle.color('red')
        else:
            turtle.color('green')
        turtle.backward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(45)
        # recursively calls function when turtle reaches end of bottom part of zigzag
        draw_zigzag(depth - 1, size / 2)
        turtle.right(45)
        # Check to see if depth % 2 == 0 when turtle goes over the line again
        if depth % 2 == 0:
            turtle.color('red')
        else:
            turtle.color('green')
        turtle.backward(size)
        turtle.left(90)
        turtle.back(size / 2)
        turtle.left(90)

def init():
    """
    Gets called to initialize the turtle
    :post-condition: Turtle's pen is up
    :post-condition: Turtle's pen size is 2.
    """
    turtle.up()
    turtle.pensize(2)


def main():
    # use user input to find out how many sets of zigzags are drawn
    depth = input("How large is the depth? ")
    # use user input to find out how large the zigzags are going to be drawn
    size = input("How large are the zigzags? ")
    # call the initialization function
    init()
    # call draw_zigzag function with user's depth and size as the parameters
    draw_zigzag(depth, size)
    print("close the canvas to quit the program")
    print("Have a nice day and thanks for the feedback!")
    turtle.done()


main()

