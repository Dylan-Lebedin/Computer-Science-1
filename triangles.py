"""
Create a function that draws a pattern of triangles using a user's specified depth and size
file: triangles.py
author: Dylan Lebedin
"""
# import turtle
import turtle

# definitions of functions and procedures


def draw_triangles(depth, size):
    """
    Draws a series of triangles
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function
    """
    depth = int(depth)
    size = int(size)
    # if depth is less than one don't do anything
    if depth < 1:
        pass
    elif depth == 1:  # if depth is equal to one only draw one triangle
        turtle.down()
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        turtle.backward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.left(60)

    else:  # if depth is more than one use recursion to draw the other triangles
        turtle.down()
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        # use recursion to draw 1st set of triangles by calling function with depth -1 and size divided by 2
        draw_triangles(depth-1, size/2)
        turtle.backward(size)
        # use recursion to draw 2nd set of triangles by calling function with depth -1 and size divided by 2
        draw_triangles(depth-1, size / 2)
        turtle.right(60)
        turtle.forward(size)
        turtle.left(60)


def init():
    """
    :post-condition: Turtle's pen is up
    :post-condition: Turtle's pen size is 2.
    """
    turtle.up()
    turtle.pensize(2)


def main():
    # use user input to find out how many sets of triangles are drawn
    depth = input("How large is the depth? ")
    # use user input to find out how large the triangles are going to be drawn
    size = input("How large are the triangles? ")
    # call the initialization function
    init()
    # call draw_triangles function with user's depth and size as the parameters
    draw_triangles(depth, size)
    turtle.done()
    print("close the canvas to quit the program")


main()

