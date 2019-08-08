#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' This module is the answer to Enso's first task of the technical questions. '''

__author__ = "Tomas Sandli Johnsen"
__version__ = "1.1"

import timeit
import functools


def sum_multiples(n):
    ''' A simple implementation of finding the sum of all multiples of 3
    and 5 from 1 to (n - 1). Count numbers that are a multiple of both
    numbers once.
    
    Complexity:
        This function is O(n)
        It performs linearly with the size of the argument
    
    Args:
        n (int): Find all multiples smaller than n and sum them
    '''

    sum = 0
    for i in range(n):
        if (i % 3) == 0:
            sum += i
        elif (i % 5) == 0:
            sum += i
    
    return sum

def sum_mutliples_optimized(n, multiples):
    ''' An optimized and generic way of finding the sum of all given
    multiples smaller than a given number n
        
    This method is based on the fact that the sum of all multiples of m
    up to n can be calculated instead of being summed through
    iteration.

    EXPLANATION:
    Example of m = 5, and n = 15:
    The multiples of 5 up to 15 are
        5, 10, 15
    Or:
        1m, 2m, 3m
    
    We see that so long as we know how many multiples we'll find, we can
    multiply the multiples with what they're a multiple of (m), and find
    the sum of all multiples.

    To know how many multiples there are, we can use integer division:
    In python3, this is represented as //. In math, there's no formal
    operator, so let's define one:
    a // b = (a - a mod b) / b

    num(m[n]):        
    15 // 3 =  3

    To find the sum of 1 + 2 + 3 + ... + n we can use:

        n        n(n + 1)
    sum(k) =  --------
    k = 1        2

    This is known from Pythegoreans as triangular numbers.
    
    3 (3 + 1)     12
    ---------  =  --  =  6
        2         2

    So now we know we have 6m, and m = 5, so the sum of all multiples is:
    6 * 5 = 30.

    Control:
    5 + 10 + 15 = 30.

    This gives us the following:
    The sum of multiple up to n:

        n        n // m (n // m + 1)
    Sum(m[n]) = -------------------- m
        k = 1             2
    
    We can't, however, simply add all the multiples of both m1 and m2,
    since we'd add up those numbers that are a multiple of both m1 and m2
    twice. So we need to find what those multiples are, and subtract them.
    Luckily, that's as easy as saying m(subtract) = m1 * m2, and use the
    same math again.


    Complexity:
        This function is O(1)
        It has a constant compute time.

    Args:
        n (int): Find all multiples smaller than n and sum them
        m (list of int): List of multiples to check for

        '''

    # The math is made to deal with "to n", not "smaller than n"
    n -= 1
    
    sum = 0
    for multiple in multiples:
        sum += (n // multiple * (n // multiple + 1)) / 2 * multiple
    
    product_of_multiples = functools.reduce(lambda x, y: x*y, multiples)
    sum -= (n // product_of_multiples * (n // product_of_multiples + 1)) / 2 * product_of_multiples

    return int(sum)

def sum_multiples_optimized_old(self, n):
    ''' This function is O(1) '''

    # since it's less than n:
    n -= 1
    
    sum = 0
    for multiple in self.multiples:
        avg = (((n // multiple) + 1) / 2) * multiple
        num = n // multiple
        sum += avg * num
    
    product_of_multiples = functools.reduce(lambda x, y: x*y, self.multiples)
    avg = (((n // product_of_multiples) + 1) / 2) * product_of_multiples
    num = n // product_of_multiples
    sum -= avg * num

    return int(sum)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == "__main__":
    n = 100000
    multiples = [3, 5]
    wrapped = wrapper(sum_multiples, n)
    print("It took {:.2f} ms to run it".format(timeit.timeit(wrapped, number=100) * 1000))
    wrapped = wrapper(sum_mutliples_optimized, n, multiples)
    print("It took {:.2f} ms to run it optimized".format(timeit.timeit(wrapped, number=100) * 1000))

    print(sum_multiples(n))
    print(sum_mutliples_optimized(n, multiples))
