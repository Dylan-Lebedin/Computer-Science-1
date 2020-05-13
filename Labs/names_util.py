"""
CSCI-141 Week 9: Dictionaries & Dataclasses
Lab: 07-BabyNames
Author: RIT CS
Author: Dylan Lebedin

This utility module is used by the main programs to perform the work on the
data and return the desired results.
"""

from dataclasses import dataclass
from operator import attrgetter, itemgetter
from typing import List


# the range of valid years of data
START_YEAR = 1880
END_YEAR = 2018

# indices into the name data when splitting by commas
NAME_INDEX = 0
GENDER_INDEX = 1
COUNT_INDEX = 2

# gender strings
FEMALE = 'F'
MALE = 'M'


def get_filename(year):
    """
    Returns a formatted string for the filename that is associated with a
    given year.
    :param year: the desired year
    :return: a string, e.g. 'yob1990.txt' if year is 1990
    """
    return f'yob{year}.txt'


"""
PROBLEM 1: tops_in_year
"""

@dataclass
class NameInfo:
    """
    A NameInfo structure is used to represent three pieces of data that are
    required by the tops_in_year main program.  For each name we want
    to record the gender and the total count of babies that were born
    in a particular year.
    """
    name: str     # baby's first name
    gender: str   # gender of baby, ('F' = female, 'M' = male)
    count: int    # total babies with the same name and gender born in a year


def get_tops_in_year(year, num):
    """
    For a particular year, find and return the top 'num' babies that were
    born in that year, sorted in descending order by counts.  By default
    'num' is 10.
    :param year: the year
    :param num: the top number of babies
    :return: a list of NameInfo objects containing the top babies for that
        year in descending order by count.
    """
    pass
    # get file for specific year
    filename = get_filename(year)
    # create empty list for all baby names of specific year
    names = []
    # create empty list for top baby names in a specific year
    final_list = []
    # open file for specific year
    file = open(filename)
    # append names list with NameInfo objects
    for line in file:
        key = line.strip().split(',')
        key[2] = int(key[2])
        name1 = NameInfo(key[0], key[1], key[2])
        names.append(name1)
    # sort names list by count
    names.sort(key=attrgetter('count'), reverse=True)
    # append final list with top baby names
    for i in range(0, num, 1):
        final_list.append(names[i])
    # close file
    file.close()
    # return final_list
    return final_list


"""
PROBLEM 2: top_name_year
"""


@dataclass
class NameCount:
    """
    A NameCount structure is used to store the information required by
    the top_name_year main program.  In the year given, the top baby
    name of the year by total count, combining both genders, is to be
    found and returned.
    """
    name: str           # baby's first name
    count: int          # total babies with the same name (combining genders) in a year
    percentage: float   # how popular was the name in relation to all babies born that year


def get_top_name_year(year):
    """
    For a given year, find and return the top name, combining both genders if
    a name appears as both female and male.
    :param year: the year
    :return: a NameCount object with the top name information
    """
    pass
    # create empty dictionary named names
    names = {}
    # find file of specific year
    filename = get_filename(year)
    # open file of specific year
    file = open(filename)
    # create max element for finding most popular name in a dictionary
    max = 0
    # create a string for the most popular name in a dictionary
    name = ''
    # create sum variable for number of people born in a year
    sum = 0
    # iterate over file and create dictionary setting name as key and value as count
    # dictionary does not depend on gender
    for line in file:
        key = line.strip().split(',')
        if key[0] in names:
            # if name is in list already add other occurrences to current value
            names[key[0]] += int(key[2])
        else:
            names[key[0]] = int(key[2])
        sum += int(key[2])
    # find name with the max count
    for i in names:
        if (max <= names[i]):
            max = names[i]
            name = i
        else:
            pass
    # find percentage name occurs in current year
    percentage = max/sum * 100
    # create object with name, count, and percentage
    name1 = NameCount(name, names[name], percentage)
    # close file
    file.close()
    # return object
    return name1

"""
PROBLEM 3: top_10_years
"""


@dataclass
class TopNamesYear:
    """
    A TopNamesYear structure is used by the top_10_years main program in order to find
    the top 'num' names over a range of years by total count.  It stores the
    female and male list of top names (strings).
    """
    females: List[str]     # list of top female names in descending order
    males: List[str]       # list of top male names in descending order


def get_top_years(start_year, end_year, num=10):
    """
    For a range of years, find and return the top 'num' female and male babies
    born over that range, in descending order.  By default 'num' is 10.
    :param start_year: the starting year (assumed to be valid)
    :param end_year: the ending year (assumed to be valid)
    :param num: the number of top names for each gender to generate
    :return: a TopNamesYear that holds the top female and male names in
    separate lists of strings.
    """
    pass
    # create empty dictionary named names
    names_female = {}
    names_male = {}
    popular_female = []
    popular_male = []
    # iterate over the files between start_year and end_year
    for i in range(start_year, end_year + 1, 1):
        filename = get_filename(i)
        file = open(filename)
        for line in file:
            key = line.strip().split(',')
            # if name is for female, add name to names_female dictionary
            if key[1] == 'F':
                if key[0] in names_female:
                    # if name is in list already add other occurrences to current value
                    names_female[key[0]] += int(key[2])
                else:
                    names_female[key[0]] = int(key[2])
            # else add name to names_male dictionary
            elif key[1] == 'M':
                if key[0] in names_male:
                    # if name is in list already add other occurrences to current value
                    names_male[key[0]] += int(key[2])
                else:
                    names_male[key[0]] = int(key[2])
            # sort list of most popular female names
            top_female = list(names_female.items())
            female = sorted(top_female, key=itemgetter(1), reverse=True)
            # sort list of most popular male names
            top_male = list(names_male.items())
            male = sorted(top_male, key=itemgetter(1), reverse=True)
        # close file
        file.close()
        # append list with top names through a given number
    for j in range(0, num, 1):
        popular_female.append(female[j][0])
        popular_male.append(male[j][0])

    top_name_year = TopNamesYear(popular_female, popular_male)
    return top_name_year