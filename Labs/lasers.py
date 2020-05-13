"""
Author: Dylan Lebedin
File: lasers.py
Laser towers game
"""

import insertion_sort
import sys


def upward_laser(index, lst):
    """
    Find the sum of an upward laser at a given index
    :param index: index of given location
    :param lst: list inputted in the function
    :return: sum of the upward laser
    """
    sum = 0
    if index - 1 >= 0 and index + 2 < len(lst):
           sum += lst[index - 1] + lst[index + 1] + lst[index + 2]
    else:
        pass

    return sum


def downward_laser(index, lst):
    """
    Find the sum of an downward laser at a given index
    :param index: index of given location
    :param lst: list inputted in the function
    :return: sum of the downward laser
    """
    sum = 0
    if index - 2 >= 0 and index + 1 < len(lst):
        sum += lst[index - 2] + lst[index - 1] + lst[index + 1]
    else:
        pass
    return sum

def laser_tower_tuple(lst1):
    """
    Creates list of sorted tuples of best location of laser towers
    :param lst1: list that will be sorted through
    :return: sorted list of tuples by descending sum
    """
    lst = []
    for i in range(1, len(lst1)):
        upward = upward_laser(i, lst1)
        downward = downward_laser(i, lst1)
        if upward >= downward:
            tup_up = (i, "upward", upward)
            lst.append(tup_up)
        else:
            tup_down = (i, "downward", downward)
            lst.append(tup_down)
        sorted_by_sum = insertion_sort.insertion_sort(lst)

    return sorted_by_sum

def read_file():
    """
    Read system arguments and output best location of lasers
    :return: Locations of best position of lasers along with orientation and sum
    """
    if len(sys.argv) != 3:
        print("Usage: lasers.py laser-file num-towers")
    else:
        lst = []
        input_file = sys.argv[1]
        file = open(input_file)
        for line in file:
            print(line)
            temp = line.split(" ")
            for t in temp:
                num = int(t)
                lst.append(num)
        file.close()
        num_lasers = int(sys.argv[2])
        print(num_lasers, "lasers", "\n")
        lst1 = laser_tower_tuple(lst)

        for i in range(0, num_lasers):
            print("Centered at location", lst1[i][0], "facing", lst1[i][1], "scoring", lst1[i][2])

def main():
    """
    Print the lasers at best locations
    :return: best lasers locations, orientations, and sums
    """
    read_file()

if __name__ == "__main__":
    main()