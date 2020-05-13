"""
Create droids from a conveyor belt, build as many as possible
author: Dylan Lebedin
file: droid_factory.py
"""

from dataclasses import dataclass
from cs_queue import enqueue
from cs_queue import dequeue
from cs_queue import make_empty_queue
from cs_queue import front

@dataclass
class Droid:
    __slots__ = 'arms', 'head', 'body', 'legs', 'serial_num'
    arms: bool
    head: bool
    body: bool
    legs: bool
    serial_num: int

def test_droid():
    """
    testing the droid dataclass
    :return: a Droid queue
    """
    new_droid = Droid(True, True, True, True, 10000)
    print(new_droid)

def read_file (filename):
    """
    read the file and create a queue, each line is another element in the queue
    :param filename: file inputted by the user
    :return: the queue created by the file contents
    """
    file = open(filename)
    conveyor = make_empty_queue()
    for line in file:
        line = line.strip("\n")
        enqueue(conveyor, line)
    file.close()
    return conveyor

def test_read_file():
    """
    test the read file function
    :return: a queue created by the file
    """
    print(read_file("droid_parts_1.txt"))

def droid_build(serial_num, conveyor):
    """
    Build a singular droid
    :param serial_num: serial number of droid
    :param conveyor: queue
    :return: a droid with correct serial number, and a head, body, arms, and legs
    """
    print("Building a new droid with the serial number", serial_num)
    new_droid = Droid(False, False, False, False, serial_num)
    while new_droid.arms is not True or new_droid.body is not True or new_droid.head is not True or new_droid.legs is not True:
        if conveyor.front.value == 'arms' and new_droid.arms == False:
            print("attaching arms...")
            new_droid.arms = True
            dequeue(conveyor)
        elif conveyor.front.value == 'legs' and new_droid.legs == False:
            print("attaching legs...")
            new_droid.legs = True
            dequeue(conveyor)
        elif conveyor.front.value == 'body' and new_droid.body == False:
            print("attaching body...")
            new_droid.body = True
            dequeue(conveyor)
        elif conveyor.front.value == 'head' and new_droid.head == False:
            print("attaching head...")
            new_droid.head = True
            dequeue(conveyor)
        else:
            front_elem = dequeue(conveyor)
            print("placing unneeded part back on belt: ", front_elem)
            enqueue(conveyor, front_elem)

    print("Droid ", serial_num, " hase been assembled!")

def test_build_droid():
    """
    test the build_droid function
    :return: 3 separate droids from the 3 files
    """
    conveyor1 = read_file("droid_parts_1.txt")
    conveyor2 = read_file("droid_parts_3.txt")
    conveyor3 = read_file("droid_parts_5.txt")
    droid_build(100, conveyor1)
    print()
    droid_build(110, conveyor2)
    print()
    droid_build(120, conveyor3)


def many_droids(conveyor):
    """
    Create as many droids as possible from the contents of the file
    :param conveyor: queue
    :return: as many completed droids as possible
    """
    print("Starting a shift at the droid factory!")
    serial_num = 10001
    while conveyor.front is not None:
        droid_build(serial_num, conveyor)
        serial_num += 1

    print("All of the droids have been assembled! Time to clock out and play Sabacc...")

def test_many_droids():
    """
    testing the many_droids function
    :return: as many droids as possible from the three files
    """
    conveyor1 = read_file("droid_parts_1.txt")
    conveyor2 = read_file("droid_parts_3.txt")
    conveyor3 = read_file("droid_parts_5.txt")
    many_droids(conveyor1)
    print()
    many_droids(conveyor2)
    print()
    many_droids(conveyor3)


def main():
    """
    have user input file and then return the droids created from the contents of the list
    :return: droids created from the contents of the list
    """
    file = input("Droid parts file: ")
    conveyor_belt = read_file(file)
    many_droids(conveyor_belt)



if __name__ == '__main__':
    #test_droid()
    #test_read_file()
    #test_build_droid()
    #test_many_droids()
    main()
