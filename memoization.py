""" Employing memoization to optimize efficiency in fib sequence recursion."""

def fib(n):

    """
    checking to see if the value is already stored in the known dict, 
    recursively identify the nth value in the fib sequence. 

    >>> fib(3)
    2

    """
    
    known = {0: 0, 1: 1}

    if n not in known:
        new_val = fib(n-1) + fib(n-2)
        known[n] = new_val

    return known[n]

print fib(3)


