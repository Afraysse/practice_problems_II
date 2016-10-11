""" 
INSERTION SORT 

"""

def insertion_sort(lst):

    for i in range(1, len(lst)):
        current = lst[i]
        place = i 

        while place > 0 and lst[place-1] > current:
            lst[place] = lst[place-1]
            place = place-1

        if place != i:
            lst[place] = current

    return lst 

print insertion_sort([3, 7, 5, 1])
