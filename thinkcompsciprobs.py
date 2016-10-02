""" RECURSION """

# dealing with koch fractals 
def koch(t, order, size):
    """ 
        Make t turtle draw a koch fractal of 'order' and 'size'. 
        Leave the turtle facing the same direction.
    """

    if order == 0:              # base case is a straight line
        t.forward(size)

    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


# Recurse a nested number list 

# NON-RECURSION
def nested_number_list(nested_lst):
    """ add up all the numbers in a nested number list. """

    total = 0 

    for i in nested_lst:
        if type(i) == type([]):
            total += sum(i)
        else:
            total += i 

    return total 

print nested_number_list([1, 2, [3, 4], 5])

# RECURSIVE 
def r_sum(nested_lst):
    """ Sum all numbers in a nested list."""

    total = 0 

    for i in nested_lst:
        if type(i) == type([]):     # calls r_sum recursively
            total += r_sum(i)       # add total += r_sum(total)
        else:
            total += i 

    return total 

print r_sum([1, 2, [3, 4], 5])

# NON-RECURISVE
def largest_value(lst):

    largest = None

    for i in lst:
        if i > largest:
            largest = i 

    return largest 

# RECURSIVE 
def largest_num(lst):

    # edge case: empty lst
    if len(lst) == 0:
        return None

    # edge case: 1 item == largest, also necessary
    elif len(lst) == 1:
        return lst[0]

    else:
        i = largest_num(lst[1:])
        return i if i > lst[0] else lst[0]


# RECURSIVE 
def largest_num(nested_lst):
    """ Find largest value in nested list."""

    largest = None 
    first_time = True

    for i in nested_lst:
        if type(i) == type([]):
            value = largest_value(i)

        else:
            value = i 

        if first_time or value > largest:
            largest = val 
            first_time = False 

    return largest

# LISTING DIRECTORY CONTENTS & SUBDIRECTORIES RECURSIVELY

import os 

def get_dirlist(path):

    """
    Will return a sorted list of all entries in path. 
    This returns just the names, not the full path to the names.
    """

    dirlist = os.listdir(path) # returns a list with entry names 
    dirlist.sort() # sorts names from file directory 
    return dirlist

def print_files(path, prefix=""):
    """ Print recursive listing of path contents."""

    if prefix = "": # detect outermost call, print heading 
        print("Folder listing for: ", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")










