"""
	Use turtle graphics to draw phrase containing word Tom
	file: write_a_meme.py
	author: Dylan Lebedin
"""

# imports the turtle module which draws pictures on a canvas window

import turtle
import math


# definitions of functions and procedures


def draw_space():
    """
        make a space between works
        :precondition: Turtle starts at the bottom right of the last letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom left of the first letter of the new word
    """
    turtle.forward(50)


def draw_a():
    """
        Draw A
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.backward(50)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(25)


def draw_h():
    """
        Draw H
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(90)
    turtle.up()
    turtle.forward(25)


def draw_l():
    """
        Draw L
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.up()
    turtle.forward(25)


def draw_m():
    """
        Draw M
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50 / math.cos(math.radians(30)))
    turtle.right(270)
    turtle.forward(50 / math.cos(math.radians(30)))
    turtle.right(135)
    turtle.forward(100)
    turtle.up()
    turtle.left(90)
    turtle.forward(25)


def draw_o():
    """
        Draw O
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(180)
    turtle.up()
    turtle.forward(25)


def draw_p():
    """
        Draw P
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.backward(50)
    turtle.forward(50)
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)


def draw_t():
    """
        Draw T
        :precondition: Turtle starts at the bottom left of the letter
        :precondition: Turtle's pen is up
        :postcondition: Turtle ends at the bottom right of the letter
    """
    turtle.forward(50)
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(25)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.backward(100)
    turtle.right(90)
    turtle.up()
    turtle.forward(50)


def init():
    """
        :postcondition: Turtle's pen is up
        :postcondition: Turtle's pen size is 2.
    """
    turtle.up()
    turtle.setup(1200, 500)
    turtle.backward(300)
    turtle.pensize(2)


def main():
    """
        The program creates the phrase ALPHA TOM
    """
    init()
    draw_a()
    draw_l()
    draw_p()
    draw_h()
    draw_a()
    draw_space()
    draw_t()
    draw_o()
    draw_m()
    turtle.done()
    print("Have a nice day!")


# now call the main function to run the program code

main()
