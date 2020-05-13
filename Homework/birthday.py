"""
file: birthday.py
author: Dylan Lebedin
Creates list of birthdays that occurred in a file more than a minimum number of times
"""

from dataclasses import dataclass

# create dataclass named Birthday with slots month, day, and year
@dataclass (frozen = True)
class Birthday:
    __slots__ = "month", "day", "year"
    # month is a string, day is a int, year is a int
    month: str
    day: int
    year: int

def num_of_occurences(filename, key):
    """
    Find the number of occurences each line occurs in the file
    :param filename: File being iterated through
    :param key: birthday date occurence
    :return: number of times a birthday occurs
    """
    count = 0
    with open(filename) as f:
        for line in f:
            #see if the key is equal to line.split and if equal increase count
            if (key == line.split()):
                count += 1

        return count

def build_dictionary(filename):
    """
    Go through file and create a dictionary based on birthdays and number of occurences in file
    :param filename: File being iterated through
    :return: Dictionary with key being the birthday and the value being the number of times it occurs
    """
    birthdays = {}
    with open(filename) as f:
        for line in f:
            key = line.split()
            # set birthday object to list indices of key
            # month is index , day is index 1, year is index 2
            birthday1 = Birthday(key[0], key[1], key[2])
            value = num_of_occurences(filename, key)
            # set birthday object as key and number of occurrences as value
            birthdays[birthday1] = value

        return birthdays

def birthdays_atleast(birthdays, min_count):
    """
    Create a list of birthdays that occur greater than or equal to the min_count
    :param birthdays: the dictionary being iterated through
    :param min_count: minimum number of occurences for a birthday to occur
    :return: list of birthdays that occurs greater than or equal to the min_count
    """
    lst = []
    for elem in birthdays.keys():
        if birthdays[elem] >= min_count:
            # append list if value at key is >= than min count
            lst.append(elem)

    return lst

def to_strings(list_birthdays):
    """
    Convert the list of birthdays to strings
    :param list_birthdays: list being iterated through
    :return: list of strings of birthdays
    """
    lst = []
    for element in list_birthdays:
        month = element.month
        day = element.day
        year = element.year

        # convert month into number
        if month == 'JAN':
            month = 1
        elif month == 'FEB':
            month = 2
        elif month == 'MAR':
            month = 3
        elif month == 'APR':
            month = 4
        elif month == 'MAY':
            month = 5
        elif month == 'JUN':
            month = 6
        elif month == 'JUL':
            month = 7
        elif month == 'AUG':
            month = 8
        elif month == 'SEP':
            month = 9
        elif month == 'OCT':
            month = 10
        elif month == 'NOV':
            month = 11
        elif month == 'DEC':
            month = 12

        # convert integers into strings
        month = str(month)
        day = str(day)
        year = str(year)

        # concatenate the string and then append string to list
        str_list = month + "/" + day + '/' + year
        lst.append(str_list)

    return lst

def main():
    # create dictionary from inputted text file
    bd_counts = build_dictionary("20000birthday.txt")
    # find the minimum count inputted by the user
    min_count = int(input("Enter a minimum count: "))
    # create list from dictionary of birthdays
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    # create list of strings of birthdays from list_birthdays
    list_strings = to_strings(list_birthdays)
    print(list_strings)


if __name__ == '__main__':
    main()
