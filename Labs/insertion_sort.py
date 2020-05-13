"""
Author: Bruce Herring
Insertion Sort
"""

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def insert(lst, unsorted_start):
    index = unsorted_start
    while index > -1 and lst[index][2] < lst[index + 1][2]:
        swap(lst, index, index + 1)
        index = index - 1

    return lst


def insertion_sort(lst):
    l = []
    for unsorted_start in range(len(lst) -1):
        l = insert(lst, unsorted_start)
    return l