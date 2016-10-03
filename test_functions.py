""" GENERAL FUNCTIONS WITH RETURN """

def area(radius):
    """ Finds the area of a circle."""
    a = 3.14159 * radius**2
    return a 

    # evaluate return expression, return the result of this function 

# can also be written, omitting temporary variable assignment
def area(radius):
    """ Finds area of a circle."""

    return 3.14159 * radius * radius 

    # temporary variables however, (b) can make debugging much easier 

# sometimes useful to have multiple return statements, one in each branch of conditional

def absolute_val(x):
    if x < 0:
        return -x
    return x 

# dead code: (unreachable code) code that appears after a return statement
# all python functions return None when they do not return a value

def find_first_2_letters(lst):
    for word in lst:
        if len(word) == 2:
            return word
    return ""

""" INCREMENTAL DEVELOPMENT """

# GOAL: avoid long debugging sessions by adding and testing small portions of code at a time 
# Example Problem: find the distance between two points, given by coordinates (x1, x2) and (y1, y2)
# The Pythagorean theorem, the distance is: distance = √(x2-x1)^2 + (y2-y1)^2

# inputs: x1, y1, x2, y2
# return value: distance (float)

# syntactically functional function 
def distance(x1, y1, x2, y2):
    """
    >>> distance(1, 2, 4, 6)
    0.0 
    """
    return 0.0 

# can add in lines of code; after each incremental change, test again 
# logical first step: find differences (x2-x1), (y2-y1)

def distance(x1, y1, x2, y2):
    """
    >>> distance(1, 2, 4, 6)
    3, 4
    """
    dx = x2 - x1
    dy = y2 - y1 
    return dx, dy

def distance(x1, y1, x2, y2):
    """
    >>> distance(1, 2, 4, 6)
    25
    """
    dx = x2 - x1
    dy = y2 - y1 
    dsquared = dx*dx + dy*dy 
    return dsquared

# use fractional exponent 0.5 to find the square root 
def distance(x1, y1, x2, y2):
    """
    >>> distance(1, 2, 4, 6)
    5.0
    """
    dx = x2 - x1
    dy = y2 - y1 
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result 

# OR 

import math 

def distance(x1, y1, x2, y2):
    """
    >>> distance(1, 2, 4, 6)
    5.0
    """
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )


""" FUNCTION COMPOSITION """

# calling one function within another

# write a function that takes two points, the center of a circle and a point on the perimeter
# and computes the area of a circle 

# (xc, yc) - center points 
# (xp, yp) - perimeter points 

radius = distance(xc, yc, xp, yp)

# find the area of a circle with that radius and return it 
result = area(radius)
return result 

# wrapping up function 
# calls two previous functions, distance and area 
def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result 

# temporary variables, radius and result are good for debugging, developing and single-stepping

# once we know it works, make it more concise:
def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))










