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

# WITH MEMOIZATION 

def fib(num):
    """
    >>> fib(3):
    2
    """

    known = {0:0, 1:1}

    if num not in known:
        value = fib(n-1) + fib(n-2)
        known[n] = value 
    return known[n]

# USING MEMOIZATION AS A DECORATOR 

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {} 

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]

    @Memoize
    def fib(n):
        for i in range(n-1):
            a,b = b, a+b
        return a 



