
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

# Tests
test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

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



