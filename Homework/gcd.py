"""
Create a function that finds the greatest common divisor for two numbers
Two functions that, one is tail-recursive, other is iterative
file: gcd.py
author: Dylan Lebedin
"""


def gcd_rec(a, b):
    """
    Function uses tail-recursion to find the gcd of inputs a and b
    :param a: first number inputted by the user
    :param b: second number inputted by the user
    :return: a if b=0; else a=b and b = a % b
    """
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return gcd_rec(b, a % b)


def gcd_iter (a, b):
    """
    Function uses iteration to find the gcd of inputs a and b
    :param a: first number inputted by the user
    :param b: second number inputted by the user
    :return: a if b=0; else a=b and b = a % b
    """
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        while (b != 0):
            temp_a = a
            temp_b = b
            a = temp_b
            b = temp_a % temp_b
            if b == 0:
                return temp_b


def test_gcd_recur():
    """
    Test the recursion gcd function
    :return: the gcd of the two inputs
    """
    print("GCD (-11, 55) = ", gcd_rec(-11, 55))
    print("GCD (21, 21) =", gcd_rec(21, 21))
    print("GCD (5, 58) =", gcd_rec(5, 58))
    print("GCD (63, 7) =", gcd_rec(63, 7))
    print("GCD (186, 17) =", gcd_rec(186, 17))
    print("GCD (20294, 12) =", gcd_rec(20294, 12))


def test_gcd_iter():
    """
    Test the iterative gcd function
    :return: the gcd of the two inputs
    """
    print("GCD (-11, 55) = ", gcd_iter(-11, 55))
    print("GCD (21, 21) =", gcd_iter(21, 21))
    print("GCD (5, 58) =", gcd_iter(5, 58))
    print("GCD (63, 7) =", gcd_iter(63, 7))
    print("GCD (186, 17) =", gcd_iter(186, 17))
    print("GCD (20294, 12) =", gcd_iter(20294, 12))


def main():
    """
    Based on the user selections, the iterative or recursive gcd function will
    be called with the two user inputs
    :return: the gcd of the two inputs using the selected function
    """
    print("Select the gcd function to use:\n")
    print("1. Recursive")
    print("2. Iterative\n")
    func_num = input("Please select a function: ")
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    num1 = int(num1)  # cast string as int
    num2 = int(num2)  # cast string as int
    result_rec = gcd_rec(num1, num2)
    result_iter = gcd_iter(num1, num2)
    if func_num == "1":
        # find the gcd using the recursive function
        print("\nThe greatest common denominator: ", result_rec, "\n")
    elif func_num == "2":
        # find the gcd using the iterative function
        print("\nThe greatest common denominator: ", result_iter, "\n")
    else:
        pass


if __name__ == "__main__":
    # Calling main function and two test functions
    main()
    test_gcd_iter()
    test_gcd_recur()


