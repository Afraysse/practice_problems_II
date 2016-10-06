""" Practice writing algorithms. """

# write a function that calculates the number of ways you could climb a
# staircase of n steps 

# n - input - number of steps
# output - return the number of ways

def staircase_traversal(n):
    """ How many different ways can you climb a staircase of n steps? 
    You can climb 1, 2, or 3 steps at a time. 
    """

    # base case: success because used exactly the right number of steps
    if n == 0:
        return 1 

    # if overshoot, not a successful path 
    if n < 1:
        return 0 

    return staircase_traversal(n - 1) + staircase_traversal(n - 2) + staircase_traversal(n - 3)


def steps_cache(n):
    """ Same Question, using memoization."""

    # Cache previous work, so don't have to keep recalculating 
    # changes the runtime from 0(3**n) to much better O(3n)

    # holds results of taking each number staircase steps 
    cache = [None] * (n+1)

    def _steps(n):

        if n < 1:
            return 0

        # if we haven't cached this yet, cache it 
        if cache[n] is None:
            cache[n] = _steps(n - 1) + _steps(n - 2) + _steps(n - 3)

        return cache[n]
    return _steps(n)



