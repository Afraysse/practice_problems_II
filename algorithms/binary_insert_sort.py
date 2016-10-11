""" Binary Insertion Sort """

def binary_search(lst, lo, hi, current):
    if lo == hi:
        if lst[lo] > current:
            return lo 
        else:
            return lo + 1

    if lo > hi:
        return lo 

    mid = (lo+hi) // 2
    if lst[mid] < current:
        return binary_search(lst, mid+1, hi, current)
    elif lst[mid] > current:
        return binary_search(lst, lo, mid-1, current)
    else:
        return mid 

def insertion_sort(lst):

    for i in range(1, len(lst)):
        current = lst[i]
        index = binary_search(lst, 0, i-1, current)
        lst = lst[:index] + [current] + lst[index:1] + lst[i+1:]

    return lst 


insertion_sort([3, 6, 3, 1])