
import time

""" LINEAR SEARCH ALGORITHM """

# Tests
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)

def search_linear(xs, target):
    """ Find and return the index of a target in sequence xs."""

    for (i,v) in enumerate(xs):
        if v == target:
            return i 
    return -1

########## LINEAR SEARCH ALGORITHM - MORE REALISTIC ################

# Runtime Complexity: O(n) - may have to scan the whole list 
# Space Complexity: O(1)

# if the list is ordered, but applying linear search - you can increment the 
# index at a faster rate (ex: 2); reduces the number of comparisons in list

# Variables
vocab = "apple boy dog down fell girl grass the tree".split(" ")
book_words = "the apple fell from the tree to the grass".split(" ")

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds not present in vocab."""
    result = [] 
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result 

def load_words_from_file(filename): 
    """ Read words from filename, return list of words."""
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()

    return wds 

bigger_vocab = load_words_from_file("vocab.txt")

print ("There are {0} words in the vocab, starting with \n {1} ".format(len(bigger_vocab), bigger_vocab[:6]))

def text_to_words(the_text):
    """ Return a list of words with punctuation removed and all in lowercase."""

    my_subs = the_text.maketrans(
        # if you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#@$%^&*{}[]()<>';:.,+=_-",
        # replace by these 
        "abcdefghijklmnopqrstuvwxyz                                   ")
    clean_text = the_text.translate(my_subs)
    wds = clean_text.split()

    return wds

def get_words_in_book(filename):
    """ Read a book from a filename, return a list of words."""
    f = open(filename, "r")
    content = f.read()
    wds = text_to_words(content)

    return wds 

book_words = get_words_in_book("AliceInWonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".format(len(book_words), book_words[:100]))

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()

print("There are {0} unknown words.".format(len(missing_words)))
print("That search took {0:.4f} seconds.".format(t1-t0))

""" BINARY SEARCH ALGORITHM """

def binary_search(xs, target):
    """ Conduct a binary search to find target from xs."""

    lb = 0              # lowerbound
    ub = len(xs)        # upperbound
    while True:
        if lb == ub:
            return -1   # list is empty 

        # else find the middle of the list 
        mid_range = (ub - lb) // 2 

        # grab item at center of list 
        mid_item = xs[mid_range]

        # check to see if item == target
        if mid_item == target:
            return mid_range        # return index of item
        if mid_item < target:
            lb = mid_range + 1      # use upper half of ROI next round
        else:
            ub = mid_range          # use lower half of ROI next round

    return mid_item

t0 = time.clock()
missing_words = binary_search(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:/4f} seconds.".format(t1-t0))

# more than 200 times faster!

# MATH COMPONENT - BINARY SEARCH ALGORITHM

from math import log, ceil 

# to calculate the number of probes (k) related to N (list size)

k = ceil(log(N + 1, 2))

# >>> ceil(log(1000 + 1, 2))
# 10.0

# BINARY SEARCH VS. DIVIDE AND CONQUER 
    # D&C should have two disjoint recursive calls (ie. QuickSort)
    # Binary search does not have this, even if it can be implemented recursively

""" REMOVING ADJACENT DUPLICATES """

def remove_adjacent_dups(xs):
    """ Using list comprehension"""
    result = []
    [result.append(i) for i in xs if i not in result]
    return result

# OR 

def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

all_words = get_words_in_book("AliceInWonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book. Only {1} are unique.".format(len(all_words), len(book_words)))
print("The first 100 are\n{0}.".format(book_words[:100]))

""" MERGE TWO SORTED LISTS. """

# Deivse an algorithm to merge two sorted lists together. 

def merge_sort(xs, ys):
    """ An inefficent method."""

    new_list = xs + ys 
    return new_list.sort()

# OR 

def merge_sort(xs, ys):

    xy = xy.insert(-1, ys)
    xy.sort()

# OR 

def merge_sort(xs, ys):

    result = []
    xi = 0
    yi = 0 

    while True:
        if xi >= len(xs):       # if xs list is finished
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result 

        # both lists still have items, copy smaller item to result 
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1 

        else:
            result.append(ys[yi])
            yi += 1

    return result 

############################## TEST FUNCTION ###################################

# test function 
def test(did_pass):
    """ Print the result of a test."""
    linenum = sys._getframe(1).f_lineno # get the caller's line number 
    if did_pass:
        msg = "Test at line {0} okay.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))

    print msg 

def test_suite():
    """ Run suite of tests for code in this module."""

    # LINEAR SEARCH ALGORITHM TESTS 
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

    # BINARY SEARCH ALGORITHM TESTS 
    xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)

    for (i,v) in enumerate(xs):
        test(search_binary(xs, v) == i)

    # REMOVING ADJACENTS ALGORITHM
    test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
    test(remove_adjacent_dups([]) == [])
    test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])

    # MERGE SORTED LISTS
    xs = [1,3,5,7,9,11,13,15,17,19]
    ys = [4,8,12,16,20,24]
    zs = xs+ys
    zs.sort()
    test(merge(xs, []) == xs)
    test(merge([], ys) == ys)
    test(merge([], []) == [])
    test(merge(xs, ys) == zs)
    test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
    test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
                   ["a", "big", "big", "bite", "cat", "dog"])
# run tests
test_suite()

