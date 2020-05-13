"""
jertle.py
Execute the given commands in turtle as read from the given file
Author:Dylan Lebedin
"""

# Notice that this program runs as is.
# It does not do anything, but that's OK.
# As you add functionality, add test functions that you call
#   instead of the main function.
# Then run main when you are ready to try some things in normal operation.
# (Remove this block of comments before submission.)

import sys
import time
import turtle

# Turtle Canvas Window Setup ######
                                  #
WORLD_SIZE = 300                  #
MARGIN = 10                       #
WINDOW_SIZE = WORLD_SIZE + MARGIN #
                                  #
###################################

SLEEP_TIME = 5

# The Set of Jertle Commands #####################################
                                                                 #
PENDOWN_CMD = "!1"  # No parameters                              #
PENUP_CMD = "!0"    # No parameters                              #
TURN_CMD = "o^"     # Parameter: angle, to the left, in degrees  #
FORWARD_CMD = "->"  # Parameter: number of units to move         #
CIRCLE_CMD = "()"   # Parameter: radius of circle                #
                                                                 #
##################################################################

### PRE-DEFINED ERROR CODES ###################################
                                                              #
ILLEGAL_COMMAND = 1  # Unrecognized command string            #
MISSING_ARGUMENT = 2 # More arguments needed for this command #
NO_ARG_END = 3       # Can't find the matching closing brace  #
                                                              #
###############################################################

def error( msg, e_code ):
    """
    A fatal error has occurred.
    Print an error message and end the program.
    :param msg: the string message to print before ending the program
    :param e_code: the integer error code with which the program exits
    """
    print( msg, file=sys.stderr )
    sys.exit( e_code )

def locate_end_of_arg(line):
    """
    Determine the index of the right brace
    :param line: the line of the program executed
    :return: the index of the right brace
    """
    for i in range(0, len(line)):
        if line[i] == "}":
            return i

def locate_start_of_arg(line):
    """
    Determine the index of the right brace
    :param line: the line of the program executed
    :return: the index of the right brace
    """
    for i in range(0, len(line)):
        if line[i] == "{":
            return i

def left_brace_error (program):
    """
    Check for command having left brace
    :param program: command of the program executed
    :return: error if missing left brace
    """\
    # check to see if length of the program is greater than 0
    if len(program) > 0:
        left = program[0]
        # check to see if the first index of the command is the left brace
        # send error if not equal
        if left != "{":
            missing_left = "Missing opening brace for argument"
            error(missing_left, MISSING_ARGUMENT)
    else:
        missing_left = "Missing opening brace for argument"
        error(missing_left, MISSING_ARGUMENT)


def right_brace_error(command, program):
    """
    Check for command having left brace
    :param program: command of the program executed
    :return: error if missing left brace
    """
    counter = 0
    new_len = len(program)
    arg = locate_end_of_arg(program)

    for i in range(len(program)):
        if program[i] == "}":
            counter += 1
        elif program[i] == "-":
            if i < new_len:
                new_len = i
        elif program[i] == "o":
            if i < new_len:
                new_len = i
        elif program[i] == "(":
            if i < new_len:
                new_len = i
        elif program[i] == "!":
            if i < new_len:
                new_len = i

    if counter == 0:
        message = "No closing brace on argument for '" + command +"'"
        error(message, NO_ARG_END)

    if arg > new_len:
        message = "No closing brace on argument for '" + command + "'"
        error(message, NO_ARG_END)




def interpret(program):
    """
    Execute the jertle commands
    :param program: string of commands
    :return: commands executed
    """
    while len(program) > 0:
        st = program[0:2]
        program = program[2:]

        item_start = locate_start_of_arg(program)
        item_end = locate_end_of_arg(program)

        if st == PENUP_CMD:
            turtle.penup()
        elif st == PENDOWN_CMD:
            turtle.pendown()
        else:
            if st == TURN_CMD:
                left_brace_error(program)
                right_brace_error(TURN_CMD, program)
                arg = int(program[item_start + 1: item_end])
                turtle.left(arg)
            elif st == CIRCLE_CMD:
                left_brace_error(program)
                right_brace_error(CIRCLE_CMD, program)
                arg = int(program[item_start + 1: item_end])
                turtle.circle(arg)
            elif st == FORWARD_CMD:
                left_brace_error(program)
                right_brace_error(FORWARD_CMD, program)
                arg = int(program[item_start + 1: item_end])
                turtle.forward(arg)
            else:
                # if not equal to one of the above commands return the command till the left brace
                ill_comm = st + program[:item_start]
                ill_comm_mess = "Illegal command '" + ill_comm + "'"
                error(ill_comm_mess, ILLEGAL_COMMAND)

        program = program[item_end+1:]

def initialize():
    """
    Set up the turtle world.
    :return: None
    """
    turtle.setup( WINDOW_SIZE, WINDOW_SIZE )
    turtle.setworldcoordinates( -MARGIN, -MARGIN, WORLD_SIZE, WORLD_SIZE )

def jertle(file):
    """
    Reads the file given for the jertle commands
    :param file: the file inputted by the user
    :return: the commands executed in the file
    """
    jertle_file = open(file)

    for line in jertle_file:
        interpret(line)

    jertle_file.close()


def main():
    """
    Read Jertle program strings from a file and execute them.
    The file is provided by the user when this program runs.
    Stop when end of file is reached.
    :return: None
    """
    initialize()
    jertle_file = input("Please input file: ")
    jertle(jertle_file)
    time.sleep(SLEEP_TIME)
    print("Please close the canvas window")
    turtle.done()

if __name__ == "__main__":
    main()
