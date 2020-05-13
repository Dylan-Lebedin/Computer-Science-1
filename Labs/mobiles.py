"""
file: mobiles.py
language: python3
author: CS.RIT.EDU
author: Dylan Lebedin
description: Build mobiles using a tree data structure.
date: 10/2015, 11/2019
purpose: starter code for the tree mobiles lab
"""

############################################################
#                                                          #
#    IMPLEMENT THE STRUCTURE DEFINITIONS PER REQUIREMENTS, #
#    AND                                                   #
#    IMPLEMENT THE MOBILE CREATION AND ANALYSIS FUNCTIONS. #
#        See the 'define structure here' text below,       #
#        the 'Create mobiles from mobile files' text,      #
#        and the heading 'mobile analysis functions'.      #
#                                                          #
#    (See also the 'pass' statements to replace.)          #
#                                                          #
############################################################

from dataclasses import dataclass
from typing import Union


############################################################
# structure definitions
############################################################

@dataclass
class Ball:
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """

    # define structure here
    __slots__ = 'cord', 'weight'
    cord: float
    weight: float


@dataclass
class Rod:
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """

    # define structure here
    __slots__ = 'leftmobile', 'leftarm', 'cord', 'rightarm', 'rightmobile'
    leftmobile: Union[Ball, 'Rod']
    leftarm: float
    cord: float
    rightarm:float
    rightmobile: Union[Ball, 'Rod']



#########################################################
# Create mobiles from mobile files
#########################################################

def read_mobile(file):
    """
    read_mobile : OpenFileObject -> Dictionary( Ball | Rod )
    read_mobile reads the open file's content and
    builds a mobile 'parts dictionary' from the specification in the file.
    The parts dictionary returned has components for assembling the mobile.
    If the mobile is a simple mobile, the returned value is
    a parts dictionary containing a Ball instance.
    If the mobile is complex, the returned value is a parts list of
    the Rod instance representing the top-most mobile component and
    the other parts.
    The connection point for each part is a string that identifies
    the key name of the part to be attached at that point.

    If there is an error in the mobile specification, then
    return an empty parts dictionary.

    # an example of the file format. 'B10' is key for the 10 oz ball.
    # blank lines and '#' comment lines are permitted.
    B10 40 10

    top B10 240 66 80 B30
    B30 55 30
    """
    # declare parts dictionary
    parts = {}
    #with open(file) as filename:
    for line in file:
            # if file contains # print out line
        if "#" in line:
                print(line, end="")
        key = line.split()
            # if length of key is 3, add ball instance
        if len(key) == 3:
            parts[key[0]] = Ball(float(key[1]), float(key[2]))
            # if length of key is 6, add Rod instance
        elif len(key) == 6:
            parts[key[0]] = Rod(key[1], float(key[2]), float(key[3]), float(key[4]), key[5])
        #else:
            #return None
    # return parts dictionary
    return parts

def construct(dict, part):
    """
    Return the mobile fully constructed based off the instances in the dictionary
    :param dict: dictionary of parts
    :param part: part instance, either rod or ball
    :return: the mobile fully constructed
    """
    # declare the mobile starting at part in dictionary
    the_mobile = dict[part]
    # if instance of ball return the mobile
    if isinstance(the_mobile, Ball):
        return the_mobile
    # if instance of Rod, return Rod instance recursively calling the left mobile arm and right mobile arm
    elif isinstance(the_mobile, Rod):
        construct_left = the_mobile.leftmobile
        construct_right = the_mobile.rightmobile
        return Rod(construct(dict, construct_left), the_mobile.leftarm, the_mobile.cord, the_mobile.rightarm, construct(dict, construct_right))
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))

def construct_mobile(parts):
    """
    construct_mobile : Dictionary( Rod | Ball ) -> Ball | Rod | NoneType

    construct_mobile reads the parts to put together the
    mobile's components and return a completed mobile object.
    The construct_mobile operation 'patches entries' in the parts.

    The parts dictionary has the components for assembling the mobile.
    Each Rod in parts has a key name of its left and right
    subordinate mobiles.  construct_mobile reads the key to
    get the subordinate part and attach it at the slot where
    the key was located within the component.

    The top mounting point of the mobile has key 'top' in parts.

    If the completed mobile object is a simple mobile, then
    the top returned value is a Ball instance.
    If the completed mobile is a complex mobile, then
    the top returned value is a Rod instance.

    If the parts dictionary contains no recognizable mobile specification,
    or there is an error in the mobile specification, then
    return None.
    """
    # call construct function with the part name being top to start at top and work downwards
    return construct(parts, "top")


############################################################
# mobile analysis functions
############################################################

def is_balanced(the_mobile):
    """
    is_balanced : Mobile -> Boolean

    is_balanced is trivially True if the_mobile is a simple ball.

    Otherwise the_mobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    # if mobile only contains ball, return true
    if isinstance(the_mobile, Ball):
        return True
    # if mobile contains rod, determine if the forces are balanced
    elif isinstance(the_mobile, Rod):
        left_side = height(the_mobile.leftmobile) * weight(the_mobile.leftmobile)
        right_side = height(the_mobile.rightmobile) * weight(the_mobile.rightmobile)
        if abs(left_side - right_side <= 1) and is_balanced(the_mobile.leftmobile) == True and is_balanced(the_mobile.rightmobile) == True:
            return True
        else:
            return False
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def weight(the_mobile):
    """
    weight : Mobile -> Number
    weight of the the_mobile is the total weight of all its Balls.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    # if only ball, return the weight
    if isinstance(the_mobile, Ball):
        return the_mobile.weight
    # if rod return weight of left mobile and right mobile
    elif isinstance(the_mobile, Rod):
        return weight(the_mobile.rightmobile) + weight(the_mobile.leftmobile)
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def height(the_mobile):
    """
    height : the_mobile -> Number
    height of the the_mobile is the height of all tallest side.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    # if only ball return the height of the cord and the diameter of the ball
    if isinstance(the_mobile, Ball):
        return the_mobile.weight + the_mobile.cord
    # if rod return cord plus max of right side or left side
    elif isinstance(the_mobile, Rod):
        return the_mobile.cord + max(height(the_mobile.leftmobile), height(the_mobile.rightmobile))
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


