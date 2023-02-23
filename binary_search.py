#!/bin/python3
'''
JOKE: There are 2 hard problems in computer science:
cache invalidation, naming things, and off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs
<= operators.
'''


def find_smallest_positive(xs, left=0, right=None):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''

    if right is None:
        right = len(xs) - 1

    if left > right:
        return None

    mid = (left + right) // 2
    if xs[mid] == 0:
        return find_smallest_positive(xs, mid + 1, right)
    elif xs[mid] < 0:
        return find_smallest_positive(xs, mid + 1, right)
    else:
        if mid == 0 or xs[mid - 1] <= 0:
            return mid
        else:
            return find_smallest_positive(xs, left, mid - 1)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''

    if len(xs) == 0:
        return 0
    if len(xs) == 1 and xs[0] == x:
        return 1

    def find_high(xs, x):
        left, right = 0, len(xs) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if xs[mid] <= x:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
                index = mid + 1
        return index

    def find_low(xs, x):
        left, right = 0, len(xs) - 1
        index = -1
        if xs[0] == x and xs[-1] == x:
            return len(xs)
        while left <= right:
            mid = (left + right) // 2
            if xs[mid] < x:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
                index = mid + 1
        return index
    return (find_low(xs, x) - find_high(xs, x))


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return hi
    m1 = (2 * lo + hi) / 3
    m2 = (lo + 2 * hi) / 3
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)


###############################################################################
# the functions below are extra credit
###############################################################################

def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum is
    guaranteed to be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''
    def helper(lo, hi):
        mid = (lo + hi) / 2
        if f(lo) < f(mid):
            return helper(lo * 2, hi)
        elif f(hi) < f(mid):
            return helper(lo, hi * 2)
        else:
            return (lo, hi)
    return helper(-1, 1)


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally uses the
    find_boundaries function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
