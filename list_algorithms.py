
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

# run tests
test_suite()












