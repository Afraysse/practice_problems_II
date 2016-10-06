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


