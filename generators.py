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





