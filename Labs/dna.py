"""
file: dna.py
author: Dylan Lebedin
description: Implement the required functions from the lab document
"""

from linked_code import concatenate
from linked_code import LinkNode
import linked_code
from linked_code import length_iter

def convert_to_nodes(DNA):
    """
    Convert a string to a linked-node structure representing the input DNA sequence
    :param DNA: string of characters corresponding to DNA bases
    :return: linked-node structure representing the input DNA sequence
    """
    # if string is empty return none
    if DNA == "":
        return None
    # else recursively call the function until completion
    else:
        return LinkNode(DNA[0], convert_to_nodes(DNA[1:]))

def convert_to_string(dna_seq):
    """
    Convert a linked-node structure of DNA bases into a string
    :param dna_seq: linked-node dna sequence
    :return: string of DNA bases
    """
    st = ''
    idx = 0
    # if link is none return empty string
    if dna_seq is None:
        return st
    # iterate through linked node and convert each value into a string and concatenate it
    while dna_seq is not None and idx <= (length_iter(dna_seq) -1):
        value = linked_code.value_at(dna_seq, idx)
        value = str(value)
        st = st + value
        idx += 1
    return st


def is_match(DNA_1, DNA_2):
    """
    Finds if two sequences are exactly the same
    :param DNA_1: dna sequence 1
    :param DNA_2: dna sequence 2
    :return: true if sequences are exactly the same, else return false
    """
    if DNA_1 is None and DNA_2 is None:
        return True
    elif DNA_1 is None or DNA_2 is None:
        return False
    elif DNA_1.value != DNA_2.value:
        return False
    else:
        return is_match(DNA_1.rest, DNA_2.rest)

def is_pairing(DNA_1, DNA_2):
    """
    Determine if the DNA bases are paired correctly
    :param DNA_1: dna sequence 1
    :param DNA_2: dna sequence 2
    :return: true if dna sequences are paired correctly and are same length, else false
    """
    if DNA_1 is None and DNA_2 is None:
        return True
    if DNA_1 is None or DNA_2 is None:
        return False
    # valid base pairing are A-T and C-G
    if linked_code.value_at(DNA_1, 0) == 'A' and linked_code.value_at(DNA_2, 0) != 'T':
        return False
    elif linked_code.value_at(DNA_1, 0) == 'T' and linked_code.value_at(DNA_2, 0) != 'A':
        return False
    elif linked_code.value_at(DNA_1, 0) == 'C' and linked_code.value_at(DNA_2, 0) != 'G':
        return False
    elif linked_code.value_at(DNA_1, 0) == 'G' and linked_code.value_at(DNA_2, 0) != 'C':
        return False
    else:
        return is_pairing(DNA_1.rest, DNA_2.rest)

def is_palindrome(dna):
    """
    Determines if dna sequence is a palindrome
    :param dna: dna sequence
    :return: true if dna sequence is a palindrome, false otherwise
    """
    if dna is None:
        return True
    first_idx = 0
    last_idx = length_iter(dna) - 1
    while dna is not None and last_idx >= first_idx:
        # determine if opposite indices are the same
        if linked_code.value_at(dna, first_idx) == linked_code.value_at(dna, last_idx):
            first_idx += 1
            last_idx -= 1
        else:
            return False
    return True

def substitution(DNA, idx, base):
    """
    Substitute a new base at a specific index
    :param DNA: dna sequence
    :param idx: index at which mutation occurs
    :param base: substituted base
    :return: linked sequence with new base at specific index
    """
    if DNA is None:
        raise IndexError("Out of Bounds")
    elif idx == 0:
        return LinkNode(base, DNA.rest)
    else:
        return LinkNode(DNA.value, substitution(DNA.rest, idx - 1, base))


def insertion(DNA_1, DNA_2, idx):
    """
    Insert dna sequence 2 at specific index of dna sequence 1
    :param DNA_1: dna sequence 1
    :param DNA_2: dna sequence 2
    :param idx: index where dna sequence 2 is being inserted at
    :return: new linked node with dna sequence 2 being inserted at specific index of dna sequence 1
    """
    if idx == 0:
        return concatenate(DNA_2, DNA_1)
    elif DNA_1 is None:
        raise IndexError("Out of Bounds")
    else:
        return LinkNode(DNA_1.value, insertion(DNA_1.rest, DNA_2, idx - 1))

def deletion(DNA, idx, size):
    """
    Delete a certain size segment from dna sequence
    :param DNA: dna sequence
    :param idx: index where deletion starts
    :param size: size of the segment being deleted
    :return: new linked-node with specific segment removed
    """
    if size == 0:
        return DNA
    elif DNA is None:
        raise IndexError("Out of Bounds")
    elif idx == 0:
        return deletion(DNA.rest, 0, size - 1)
    else:
        return LinkNode(DNA.value, deletion(DNA.rest, idx - 1, size))

def duplication(DNA, idx, size):
    """
    Insert duplicate segment of specific size at index of idx + size
    :param DNA: dna sequence
    :param idx: index where dna sequence starts to be copied
    :param size: size of segment copied
    :return: new linked-node with duplicate segment of specific size inserted at index of idx + size
    """
    if size == 0:
        return DNA
    elif DNA is None:
        raise IndexError("Out of Bounds")
    lnk = None
    for i in range(size):
        val = linked_code.value_at(DNA, i + idx)
        lnk = linked_code.insert_at(i, val, lnk)
    new_link = insertion(DNA, lnk, idx + size)
    return new_link


