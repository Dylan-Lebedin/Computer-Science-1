"""
Create a picture of colorful squares based off the characters in a song
file: songs.py
author: Dylan Lebedin
"""

#import turtle
import turtle

# definitions of functions and procedures
def square(color):
    """
    draw square of color inputted by user
    :param color: color that is inputted by the user
    """
    turtle.up()
    turtle.color(color)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.up()


def paint_line(song_line):
    """
    Draw a row of colorful squares based off the UCS2 values of the characters in the song line
    :param song_line: song line from file
    :return: row of colorful squares for the song line
    """
    for ch in range(len(song_line)):
        if ord(song_line[ch]) < 70:
            square("darkorchid")
        elif ord(song_line[ch]) >= 70 and ord(song_line[ch]) < 100:
            square("chartreuse")
        elif ord(song_line[ch]) >= 100 and ord(song_line[ch]) < 110:
            square("cyan")
        elif ord(song_line[ch]) >= 110 and ord(song_line[ch]) < 122:
            square("crimson")
        else:
            square("darkorange")

    turtle.back(10*len(song_line))
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

def picture(filename):
    """
    Opens file and draws picture based on contents of the file
    :param filename: file that will be analyzed
    :return: picture of colorful squares
    """
    file = open(filename)

    for line in file:
        paint_line(line)

    file.close()

def init ():
    """
    Initialize turtle speed to 0
    Accelerate drawing by using turtle.tracer()
    """
    turtle.speed(0)
    turtle.tracer(100, 30)
    turtle.up()
    turtle.goto(-350, 300)
    turtle.down()

def main():
    """
    Initialize the turtle
    Draw picture based on user input file
    :return: picture of colorful squares
    """
    filename = input("Please input the filename: ")
    init()
    picture(filename)
    print("Close the canvas to quit the program")
    turtle.done()


if __name__ == "__main__":
    # Calling main function and two test functions
    main()


