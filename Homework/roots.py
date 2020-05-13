"""
	Create a function that computes the real roots of a quadratic equation, prints the equation
    and the number of roots.
	file: roots.py
	author: Dylan Lebedin
"""

# imports the math module for using the square root function

import math

# definitions of functions and procedures


def quadratic_roots(a, b, c):
    """
        Finds the quadratic roots of an equation inputted by the user
        Prints equation in form ax^2+bx+c
        Finds the value of b^2 - 4ac
        If it is positive, there are two roots. If it’s zero, there is one root. If it is negative, there are
        no roots.
        Prints the results of the quadratic equation
    """

    print("Equation:", a, "x^2 + ", b, "x + ", c, " = 0")

    num_roots = (b**2) - (4*a*c)

    if num_roots >= 0:  # won't allow for imaginary numbers if num_roots < 0
        quadratic_result_positive = (-1 * b + math.sqrt(num_roots)) / (2 * a)
        quadratic_result_negative = (-1 * b - math.sqrt(num_roots)) / (2 * a)

    if num_roots > 0:  # will print two roots
        print("Two roots.")
        print("X = ", quadratic_result_positive)
        print("X = ", quadratic_result_negative, "\n")
    elif num_roots < 0:  # will print no roots
        print("No roots.\n")
    else:  # will print one root
        print("One root.")
        print("X = ", quadratic_result_positive, "\n")


def main():
    """
        The program uses the users inputs and plugs them in to the quadratic_roots function
        Will tell the user their equation, the number of roots it has, and the values of the roots
    """
    num1 = int(input("What is your first number? "))  # ax^2 value
    num2 = int(input("What is your second number? "))  # bx value
    num3 = int(input("What is your third number? "))  # c value

    quadratic_roots(num1, num2, num3)
    quadratic_roots(1, 10, 25)  # test 1
    quadratic_roots(-3, -36, -60)  # test 2
    quadratic_roots(1, 4, 4)  # test 3
    quadratic_roots(-2, 9, 18)  # test 4
    quadratic_roots(5, 15, -25)  # test 5
    quadratic_roots(6, 14, 21)  # test 6
    quadratic_roots(8, 13, 81)  # test 7
    quadratic_roots(2, -23, 45)  # test 8
    quadratic_roots(5, 13, 65)  # test 9
    quadratic_roots(1, -6, 9)  # test 10

# now call the main function

main()
