"""
Create a scene that includes a pond
Inside the pond are a number of raindrops which are inputted by the user
Around the raindrops are a randomly generated number of ripples
file: raindrops.py
author: Dylan Lebedin
"""
# import turtle, math, and random
import turtle
import math
import random

# global variables
MAX_RAINDROPS = 100  # max amount of raindrops in pond
MAX_RADIUS = 20  # max radius of a raindrop in pond
MAX_RIPPLES = 8  # max number of ripples around a raindrop
MIN_RIPPLES = 3  # min number of ripples around a raindrop
pond_size = 500  # size of the pond


# definitions of functions and procedures
def draw_pond():
    """
    Draws boundaries of the pond
    """
    turtle.up()
    turtle.forward(pond_size/2)
    turtle.left(90)
    turtle.color("dodger blue")
    turtle.begin_fill()
    turtle.down()
    turtle.forward(pond_size/2)
    turtle.left(90)
    turtle.forward(pond_size)
    turtle.left(90)
    turtle.forward(pond_size)
    turtle.left(90)
    turtle.forward(pond_size)
    turtle.left(90)
    turtle.forward(pond_size/2)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(pond_size/2)
    turtle.right(180)
    turtle.color("black")


def raindrop():
    """
    Creates a raindrop and ripples around the raindrop
    :return: circumference of raindrop
    """
    turtle.up()
    # create a raindrop with a radius between 1 and 20
    radius = random.randint(1, MAX_RADIUS)
    # number of ripples are between 3 and 8
    ripples = random.randint(MIN_RIPPLES, MAX_RIPPLES)
    # have the raindrop and its ripples fit in the pond's boundaries
    # set the turtle at the random position in the boundaries
    pos_x = random.randint(-pond_size/2 + (radius*2 + radius*ripples), pond_size/2 - (radius*2 + radius + radius*ripples))
    pos_y = random.randint(-pond_size/2 + (radius*2 + radius*ripples), pond_size/2 - (radius*2 + radius*ripples))
    turtle.setpos(pos_x, pos_y)
    # fill the raindrop with a color and have outline be black
    turtle.fillcolor(random.random(), random.random(), random.random())
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.down()
    turtle.circle(radius)
    turtle.end_fill()
    # set count = 2 since first ripple is twice the radius of the circle
    count = 2
    # set initial circumference to 0
    circumference = 0
    while ripples > 0:
        turtle.down()
        turtle.right(90)
        turtle.up()
        # move forward by radius of circle
        turtle.forward(radius)
        turtle.left(90)
        new_radius = radius * count
        turtle.down()
        # draw circle with radius of original radius * count
        turtle.circle(new_radius)
        # find circumference of the ripples
        circumference += (new_radius * math.pi * 2)
        # decrease number of ripples by 1 and increase counter by 1
        ripples -= 1
        count += 1
        turtle.up()
    # return circumference of the ripples
    return circumference


def rec_raindrops(num_raindrops, circ_sum):
    """
    Recursively call the raindrop function
    :param num_raindrops: uses num_raindrop function from raindrops function to figure
    out how many raindrops to draw
    :param circ_sum: total circumference of ripples
    :return: total circumference of all the raindrops ripples
    """
    if num_raindrops <= 0:
        pass
    else:
        circ_sum += raindrop()
        rec_raindrops(num_raindrops-1, circ_sum)
    return circ_sum


def main():
    """
    Has user input number of raindrops to draw, and draws that number of raindrops
    with ripples around each raindrop
    :return: the total circumference of all the ripples around each raindrop
    """
    num_raindrops = input("Raindrops (1-100): ")
    num_raindrops = int(num_raindrops)
    while num_raindrops > MAX_RAINDROPS:
        print("Raindrops must be between 1 and 100 inclusive.")
        num_raindrops = input("Raindrops (1-100): ")
        num_raindrops = int(num_raindrops)

    draw_pond()
    total_circumference = rec_raindrops(num_raindrops, 0)
    print("The total circumference of all the ripples is ", total_circumference, "units.")

    print("Close the canvas to quit the program")
    turtle.done()


if __name__ == "__main__":
    # Calling main function and two test functions
    main()

