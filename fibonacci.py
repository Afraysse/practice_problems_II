""" MULTIPLE WAYS OF COMPLETING FIBONACCI PROBLEMS."""

# ITERATIVE SOLUTION

def fib(n):
    """
    >>> fib(3)
    2

    """

    a,b = 1,1

    for i in range(n-1):
        a,b = b,a+b
    return a

print fib(4)

# RECURSIVE SOLUTION

def fib(n):
    """
    >>> fib(3)
    2

    """

    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)

print fib(4)

# OR

def fib(n):
     """
    >>> fib(3)
    2
    
    """

    if n==1 or n==2: 
        return 1 

    return fib(n-1) + fib(n-2)

print fib(4)

# WITH GENERATORS 

a,b = 0,1
def fib():
    global a,b # all references to a,b are referenced back to the global namespace
    while True:
        a,b = b, a+b
        yield a 

fib()
fib.next()
fib.next()
fib.next()
fib.next()
print fib.next()



















