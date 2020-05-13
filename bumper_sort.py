"""
file: bumper_sort.py
author: Dylan Lebedin
purpose: Implementation of the bumper-sort algorithm
"""
from merge_sort import merge_sort
from quick_sort import quick_sort
import random
import time

def max_value(data, size):
    """
    Find the max value in the list data
    :param data: list being iterated through
    :param size: size of list data
    :return: max value of list data
    """
    max_val = data[0]
    for i in range(1, size-1):
        if data[i] > max_val:
            max_val = data[i]

    return max_val


def bumper_sort (data, k):
    """
    Create the bumper_sort algorithm
    :param data: list of numbers
    :param k: max value in list data
    :return: result and histogram
    """
    size = k + 1
    # create list named hist with size k + 1
    #initialize all elements of hist to 0
    hist = [0] * size

    # populate hist with the number of times each element in data occurs
    for num in range(0, len(data)):
        hist[data[num]] += 1

    # make new list named result that is the sorted version of data
    result = []
    for i in range(0, len(hist)):
            result_val = hist[i]
            for j in range(0, result_val):
                result.append(i)

    return result


def main():
    """
    Sort the lists using bumper_sort, and output the time it takes for each sorting algorithm to sort the large lists
    :return: lists and sorted and sorting times
    """
    small_list = [2, 5, 3, 0, 2, 3, 0, 3]
    max_val_small = max_value(small_list, len(small_list))
    result_small_list = bumper_sort(small_list, max_val_small)
    print("Small list, unsorted: ", small_list)
    print("Small list, bump-sorted: ", result_small_list)

    thou_list = []
    size = 1000
    for i in range(0, size):
        thou_list.append(random.randrange(0, 300))

    max_val_thou = max_value(thou_list, len(thou_list))
    result_thou_list = bumper_sort(thou_list, max_val_thou)
    print("Big list, unsorted: ", thou_list)
    print("Big list, bump-sorted: ", result_thou_list)

    print("\nSorting a randomized list of", len(thou_list), "elements")
    start = time.process_time()
    answer = merge_sort(thou_list)
    end = time.process_time()
    print("merge_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = quick_sort(thou_list)
    end = time.process_time()
    print("quick_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = bumper_sort(thou_list, max_val_thou)
    end = time.process_time()
    print("bumper_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = sorted(thou_list)
    end = time.process_time()
    print("sorted time: ", end - start, " seconds")

    million_list = []
    size = 1000000
    for i in range(0, size):
        million_list.append(random.randrange(0, 300))

    max_val_mill = max_value(million_list, len(million_list))

    print("\nSorting a randomized list of", len(million_list), "elements")
    start = time.process_time()
    answer = merge_sort(million_list)
    end = time.process_time()
    print("merge_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = quick_sort(million_list)
    end = time.process_time()
    print("quick_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = bumper_sort(million_list, max_val_mill)
    end = time.process_time()
    print("bumper_sort time: ", end - start, " seconds")

    start = time.process_time()
    answer = sorted(million_list)
    end = time.process_time()
    print("sorted time: ", end - start, " seconds")


if __name__ == '__main__':
    main()





