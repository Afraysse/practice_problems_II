""" REVERSE A STRING RECURSIVELY """

def reverse_string(string):

    output = ""
    if len(string) == 0:
        return output

    output += string[-1]
    return output + reverse_string(string[:-1])

""" REVERSE STRING WITH INDEXES """

def reverse_string_indexes(string):

    return string[::-1]

""" SUM ITEMS IN A LIST - BRUTE FORCE """

def sum_items_in_lst(lst):

    sum_items = 0 

    for i in lst:
        sum_items += i 

    return sum_items

""" SUM ITEMS RECURSIVELY """

def sum_items_in_lst_recurse(lst):

    sum_items = 0 
    if lst == []:
        return sum_items
    sum_items += lst[0]
    return sum_items + sum_items_in_lst_recurse(lst[1:])


""" MERGE SORT SORTED LISTS """

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
def merge_sort(lst1, lst2):
    """ Merge together two sorted lists. """

    x = 0
    y = 0 
    results = []

    while True:
        if y >= len(lst1):
            results.extend(lst1[x:])
            return results

        if x >= len(lst2):
            results.extend(lst2[y:])
            return results

        if lst1[x] <= lst2[y]:
            results.append(lst1[x])
            x += 1 

        if lst2[y] <= lst1[x]:
            results.append(lst2[y])
            y += 1 

""" POLISH NOTATION CALCULATOR. """

# s = "/ 6 - 4 2"
def polish_notation(s):
    """ Calculate (s) where s as a string is the equation."""

# iterate through list - see if int or symbol 
# the first item should be a symbol 
# the last item should be a num 

# could either put into a new string or a list 

    new = s.split(" ")






    













