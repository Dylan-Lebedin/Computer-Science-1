"""
file: linked_insort.py
author: Dylan Lebedin
description: insertion sort of linked lists and prints in a pretty format
"""

from linked_code import LinkNode
from linked_code import length_iter


def insert(value, lnk):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    # if link is empty put value at front of linked list
    # exit()
    if lnk is None:
        return LinkNode(value, None)
    # if value is greater than linked list value, insert value at end of linked list
    elif lnk.value >= value:
        return LinkNode(value, lnk)
    # else iterate through linked list until value is placed in the linked list
    else:
        return LinkNode(lnk.value, insert(value, lnk.rest))


def insort(lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    sorted_lnk = None
    while lnk is not None:
        sorted_lnk = insert(lnk.value, sorted_lnk)
        lnk = lnk.rest
    return sorted_lnk


def pretty_print(lnk):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    st = '['
    while lnk is not None:
        if length_iter(lnk) > 1:
            st += str(lnk.value) + ', '
            lnk = lnk.rest
        else:
            st += str(lnk.value)
            lnk = lnk.rest
    st += ']'
    print(st)
