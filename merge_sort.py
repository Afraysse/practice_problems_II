import time 
from list_algorithms import get_words_in_book, remove_adjacent_dups

""" FURTHER STUDY ON MERGE SORT ALGORITHM """

# Adapting the merge algorithm pattern for different cases 

# Return only items present in both lists 
def merge_sort_return_same(xs, ys):
    """ Return items present in both lists."""

    result = []
    identical = []
    xi = 0 
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return identical

        if yi >= len(ys):
            result.extend(xs[xi:])
            return identical

        # both lists still have items, copy smaller items to result 
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1 

        elif ys[yi] < xs[xi]:
            result.append(ys[yi])
            yi += 1 

        else:
            if ys[yi] == xs[xi]:
                identical.append(ys[yi])
                result.append(xs[xi])
                yi += 1
                xi += 1 

# return words found in the book not in the vocabulary 
def find_unknown_merge_pattern(vocab, wds):
    """ Sort both the vocab and word lists. Return a new list of words from 
    wrds that do not appear in vocab list.
    """

    result = [] 
    xi = 0 
    yi = 0 

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result 

        if yi >= len(wds):
            return result 

        if vocab[xi] == wds[yi]:        # word present in vocab
            yi += 1 

        elif vocab[xi] < wds[yi]:       # move past vocab word
            xi += 1 

        else:
            result.append(wds[yi])      # grab word not in vocab
            yi += 1 


# put together with previous texts
all_words = get_words_in_book("AliceInWonderland.txt")
t0 = time.clock()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknown_merge_pattern(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))



