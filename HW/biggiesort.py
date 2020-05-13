"""
File: biggiesort.py
Author: Dylan Lebedin
1. In a test case where the list is in sequential order, insertion sort will perform better than biggie sort.
2. Biggie sort sort has to go through the list each time, from the point where it currently is.
    In a case where the list is ordered it will have to go to the end of the list each time.
    The time complexity for this case for insertion sort is O(N), while for reverse selection sort it is O(N^2)
"""


def find_max_index(lst, a, b):
    """
    Find the max index between the given indices of the list
    :param lst: list being iterated through
    :param a: index 1
    :param b: index 2
    :return: the index of the max value between the two indices
    """
    lst = lst[a : b + 1]
    max_index = 0
    for i in range(len(lst)):
        if lst[max_index] < lst[i]:
            max_index = i

    return max_index


def swap(lst, a, b):
    """
    Swap the given values in the list
    :param lst: list whose values are being swapped
    :param i: value 1
    :param j: value 2
    :return: swapped values of list
    """
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def biggiesort(lst):
    """
    Sort the list by ascending order finding the max value first
    :param lst: list being sorted
    :return: list sorted in ascending order
    """
    for mark in range(len(lst)-1,0, -1):
        swap(lst, mark, find_max_index(lst,0, mark))

    return lst

def read_file(input_file):
    """
    Read file inputted by user and sort the list of values in file
    :param input_file: file inputted by the user
    :return: sorted list
    """
    lst = []
    file = open(input_file)
    for line in file:
        temp = int(line.strip())
        lst.append(temp)
    file.close()
    print("Sorting File: ", input_file)
    print("Unsorted: ", end="")
    print(lst)
    print("Sorted: ", end="")
    print(biggiesort(lst))

def main():
    """
    User inputs file, and file is sorted
    :return: Sorted file in a list
    """
    file = input("Enter File Name: ")
    read_file(file)

if __name__ == "__main__":
    main()
