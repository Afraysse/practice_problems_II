""" GENERATORS: used to generate a series of values. 

'yield' = akin to return statement, only does not save the 'state' of a generator function 
    - yield implies transfer of control is temporary and voluntary; as opposed to return'special 
    'returning control' at the conclusion of a subroutine (ie: function)
'generator' = relational to a special type of iterator 
.next() - similar to iterators, we can get the next value from a generator by using .next() 
for - gets values by calling .next() implicitly 

"""

# WITHOUT GENERATORS 
def get_primes(input_list):

    """ 
    Take an input list of numbers and return some iterable containing the elements
    which are prime numbers.

    Iterable is just an object capable of returning its members one at a time.

    >>> input_list = [2, 3, 4, 6, 7]
    [2, 3, 7]
    """

    return (i for i in input_list if is_prime(i))

def is_prime(num):

    if num > 1:
        if num == 2:
            return True 
        if num % 2 == 0:
            return False 
        for current in range(3, int(math.sqrt(num) + 1), 2):
            if num % current == 0:
                return False 
        return True
    return False 

# WITH GENERATORS

""" 
Scenario Change: dealing with a large body of data and memory management. 

Call instead with a 'start' argument and return all prime nums > start.  

Quandry: can't return all nums from start to inifinity. 

Solution: functions return all nums at once because they only get one chance
to return. What if they didn't return that way? 

Instead, return the next value (.next()) instead of all values at once. Eschew
creating a list to store (reduction of memory issues). 

Generator function - "generates values" - akin to a normal function only 
whenever it needs to generate a function, it does so with 'yield' (vs 'return')

To get a value from a generator, we use the same built-in function for 
iterators: .next() 

"""

# REVISED GENERATOR GET_PRIMES
def get_primes(num): 
    while True:
        if is_prime(num):
            yield num 
        num += 1 

def solve_number_10():
    total = 2
    for next_prime in get_primes(num):  # num = 3, for example below
        if next_prime < 200000:
            total += next_prime
        else:
            print(total)
            return 

"""
1. Enter for loop in solve_number_10; requests the first number from 
get_primes 
2. Enter get_primes as you would in a normal function:
    a. Enter the while loop on second line of get_primes
    b. The if condition holds true (3 is prime)
    c. Yield the value (3) and control to solve_number_10
3. Return to solve_number_10:
    a. Value (3) is passed back to the for loop 
    b. For loop assigns next_prime to this value
    c. next_prime is added to total 
    d. for loop requests the next item in get_primes

"""


















