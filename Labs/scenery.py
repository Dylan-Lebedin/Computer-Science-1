"""
Create a scene that includes two houses and a tree
file: scenery.py
author: Dylan Lebedin
Partners: Banyan Batts, Gunnar Bachmann, Jaylan Sanford, Phuong Nguyen
"""

# imports the math module for using the square root function

import turtle
import math

# definitions of functions and procedures

def draw_rect(length, width, color_rect):
    """
    Draws a rectangle
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function
    """
    turtle.down()
    turtle.color(str(color_rect))
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(180)
    turtle.end_fill()
    turtle.up()


def draw_isosceles_triangle(length, width, height, color_triangle):
    """
    Draws a isosceles triangle
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function
    """
    # use pythagorean theorem to find the side-lengths of the triangle
    side_length = math.sqrt(((width/2)**2) + (height**2))
    # use trigonometry to find the angle between the side-length and the base
    angle_one = math.degrees(math.asin(height/side_length))
    # find the angle between the two side lengths of the triangle
    angle_two = 180 - (2*angle_one)
    turtle.up()
    turtle.color(str(color_triangle))
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(length)
    turtle.down()
    turtle.right(90)
    turtle.left(angle_one)
    turtle.forward(side_length)
    turtle.right(180-angle_two)
    turtle.forward(side_length)
    turtle.right(180-angle_one)
    turtle.forward(width)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(length)
    turtle.left(90)

def draw_door(length, width, color_door):
    """
    Draws a door at the center of the house
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function, then translated by the width + 100 units
    """
    turtle.up()
    turtle.forward(width/2-width/10)
    turtle.left(90)
    turtle.down()
    turtle.color(str(color_door))
    turtle.begin_fill()
    turtle.forward(length/3)
    turtle.right(90)
    turtle.forward(2*width/10)
    turtle.right(90)
    turtle.forward(length/3)
    turtle.right(90)
    turtle.up()
    turtle.forward((width/2) + width/10)
    turtle.end_fill()
    turtle.right(180)
    turtle.up()


def draw_windows(length, width, color_windows):
    """
    Draws windows
    Two stories if length > width, otherwise only one story
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function, then translated by the width + 100 units
    """
    if (length > width):  # draws two stories worth of windows
        turtle.forward(width/2 - 4*width/10)
        turtle.left(90)
        turtle.forward(length/3 - length/10)
        turtle.right(90)
        draw_rect(length/10, width/10, color_windows)
        turtle.left(90)
        turtle.forward(length/3)
        turtle.right(90)
        draw_rect(length / 10, width / 10, color_windows)
        turtle.forward(width/2 + 2*width/10)
        draw_rect(length / 10, width / 10, color_windows)
        turtle.right(90)
        turtle.forward(length/3)
        turtle.left(90)
        draw_rect(length / 10, width / 10, color_windows)
        turtle.right(90)
        turtle.forward(length/3 - length/10)
        turtle.left(90)
        turtle.backward(width/2 + 3*width/10)

    else:  # else draw one story worth of windows
        turtle.forward(width / 2 - 4 * width / 10)
        turtle.left(90)
        turtle.forward(length / 2 - length / 5)
        turtle.right(90)
        draw_rect(length / 5, width / 10, color_windows)
        turtle.forward(width / 2 + 2 * width / 10)
        draw_rect(length / 5, width / 10, color_windows)
        turtle.right(90)
        turtle.forward(length / 2 - length / 5)
        turtle.left(90)
        turtle.backward(width / 2 + 3 * width / 10)


def draw_house(length, width, height, color_facade, color_roof, color_door, color_windows):
    """
    Draws a house, a triangle on top of a rectangle with windows and a door
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function, then translated by the width + 100 units
    """
    turtle.down()
    draw_rect(length, width, color_facade)  # facade
    draw_door(length, width, color_door)  # door
    draw_isosceles_triangle(length, width, height, color_roof)   # roof
    draw_windows(length, width, color_windows)  # windows
    turtle.up()
    turtle.forward(width + 100)

    area = length*width  # returns the area of the facade of the house
    return area


def draw_tree(trunk, diameter, color_tree):
    """
    Draws a tree, a circle on top of a rectangle
    :precondition: Turtle is pointing towards the east
    :precondition: Turtle's pen is up
    :post-condition: Turtle's state is the same as at start of the function, then translated by the diameter + 100 units
    """
    turtle.down()
    turtle.color(str(color_tree))
    draw_rect(trunk, diameter, color_tree)  # creates rectangle for circle to be on top of
    turtle.begin_fill()
    turtle.down()
    turtle.left(90)
    turtle.forward(trunk)
    turtle.right(90)
    turtle.forward(diameter/2)
    turtle.circle(diameter)
    turtle.end_fill()
    turtle.up()
    turtle.forward(diameter/2)
    turtle.right(90)
    turtle.forward(trunk)
    turtle.left(90)
    turtle.up()
    turtle.forward(diameter + 100)

def init():
    """
    :post-condition: Turtle's pen is up
    :post-condition: Turtle's pen size is 2.
    :post-condition: Turtle's position is moved back by 200 units
    """
    turtle.up()
    turtle.pensize(2)
    turtle.backward(500)
    turtle.setworldcoordinates(-5, -5, 1405, 1405)
    turtle.screensize(700, 700)

def main():
    """
    Draws two houses and a tree
    Also computes which facade is bigger out of the two by comparing areas
    """
    init()
    draw_tree(150,20, 'aqua')
    area1 = draw_house(150, 100, 50, 'orange', 'blue', 'purple', 'teal')
    area2 = draw_house(80, 150, 100, 'purple', 'brown', 'green', 'black')
    draw_tree(70, 20, 'blue')
    if (area1 > area2):
        print("big facade is ", area1, "square \"units\".")
        print("small facade is ", area2, "square \"units\".")
    else:
        print("big facade is ", area2, "square \"units\".")
        print("small facade is ", area1, "square \"units\".")

    turtle.done()
    print("close the canvas to quit the program")


main()

