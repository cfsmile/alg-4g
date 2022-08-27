#!/usr/bin/env python
# -*- encoding:UTF-8 -*-

# Google pystyle : https://google.github.io/styleguide/pyguide.html
# use sphinx build a documentation.
# https://blog.csdn.net/lixiaomei0623/article/details/120530642
# TODO:https://stackoverflow.com/questions/52466582/sphinx-doesnt-parse-rst-docstrings-correctly

import doctest

def gcd0(p: int, q: int) -> int:
    """Calculate greatest common divider of two numbers with Brute force 
    algorithm.
    
    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, 
        then return non-zero one
    
    >>> gcd0(6, 4)
    2
    >>> gcd0(7, 5)
    1
    >>> gcd0(10, 5)
    5
    >>> gcd0(60, 24)
    12
    >>> gcd0(0, 8)  # TODO : this cannot pass
    8
    """
    t = 1 # if p is 0 the for loop will not execute. directly return c
    # i is all the possible common divider of p and q
    for i in range(1, (min(p,  q) + 1)):  
    # +1 will include the minimal int such as 5 in (10, 5)
        if ((p % i) == 0) and ((q % i) == 0):
            if t < i:
                t = i
    return t

def gcd1(p: int, q: int) -> int:
    """Calculate greatest common divider of two numbers with prime 
    factorization algorithm.

    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, 
        then return non-zero one
    
    >>> gcd1(6, 4)
    2
    >>> gcd1(7, 5)
    1
    >>> gcd1(10, 5)
    5
    >>> gcd1(60, 24)
    12
    >>> gcd1(0, 8)  # TODO : this cannot pass
    8
    """
    t = 1 # if p is 0 the for loop will not execute. directly return c
    # i is all the possible common divider of p and q
    for i in range(2, (min(p,  q) + 1)):  
    # +1 will include the minimal int such as 5 in (10, 5)
        while ((p % i) == 0) and ((q % i) == 0):
            t = t * i
            p =  p // i
            q =  q // i
    return t


def gcd2(p: int, q: int) -> int:
    """Calculate greatest common divisor of two numbers.

    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, 
        then return non-zero one
    
    >>> gcd2(6, 4)
    2
    >>> gcd2(7, 5)
    1
    >>> gcd2(10, 5)
    5
    >>> gcd2(60, 24)
    12
    >>> gcd2(0, 8)
    8
    """
    assert p > 0 , "0 cannot be a divider"
    assert q > 0 , "0 cannot be a divider"
    t = min(p,  q)
    # while t >= 1:
    #     if (p % t) == 0:
    #         if (q % t) == 0:
    #             return t
    #         else:
    #             t -= 1 
    #     else:
    #         t -=1
    while t >= 1:
        if ((p % t) == 0) and ((q % t) == 0):
            return t
        else:
            t -= 1 
    return t

def gcd3(p: int, q: int) -> int:
    """Calculate greatest common divisor of two numbers with Euclidean 
    algorithm.

    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, then return non-zero one

    >>> gcd3(6, 4)
    2
    >>> gcd3(7, 5)
    1
    >>> gcd3(10, 5)
    5
    >>> gcd3(0, 8)
    8
    """
    if p == q == 0:
        return 0
    if p == 0 or q == 0:
        return p if q == 0 else q
    return p if q == 0 else gcd3(q, p % q)

def gcd4(p: int, q: int) -> int:
    """Calculate greatest common divisor of two numbers with the stein 
    algorithm.
    https://www.geeksforgeeks.org/steins-algorithm-for-finding-gcd/

    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, then return non-zero one

    >>> gcd4(6, 4)
    2
    >>> gcd4(7, 5)
    1
    >>> gcd4(10, 5)
    5
    >>> gcd4(0, 8) 
    8
    """
    
    # gcd(0, q) == q, gcd(p, 0) == p, gcd (0, 0) == 0
    if p == 0:
        return q
    if q == 0:
        return p
    # Finding K, where K is the greatest power of 2 that divides both p and q
    k = 0
    while ((( p | q) & 1) == 0):
        p = p >> 1
        q = q >> 1
        k += 1
    # Dividing p by 2 until p becomes odd
    while ((p & 1) == 0):
        p = p >> 1
    # From here on , p is always odd.
    while(q != 0):
        # if q is even, remove all factor of 2 in p
        while((p & 1) == 0):
            p = p >> 1
        # Now p and q are both odd. Swap if necessary so p<=q, then 
        # set q = q - p(which is even).
        if (p > q):
            # swap p and q
            p, q = q, p
        q = q - p
    # restore common factors of 2
    return (p << k)
        
def gcd5(p: int, q: int) -> int:
    """Calculate greatest common divisor of two numbers with the stein
    algorithm.
    https://www.geeksforgeeks.org/steins-algorithm-for-finding-gcd/

    Args:
        p (int): integer input
        q (int): integer input

    Returns:
        int: greatest common divider, if p or q is 0, then return non-zero one

    >>> gcd5(6, 4)
    2
    >>> gcd5(7, 5)
    1
    >>> gcd5(10, 5)
    5
    >>> gcd5(0, 8) # this is 
    8
    """
    if (p == q):
        return p
 
    # GCD(0, q) == q; GCD(p, 0) == p,
    # GCD(0, 0) == 0
    if (p == 0):
        return q
 
    if (q == 0):
        return p
 
    # look for factors of 2
    # p is even
    if ((~p & 1) == 1):
 
        # q is odd
        if ((q & 1) == 1):
            return gcd5(p >> 1, q)
        else:
            # both a and b are even
            return (gcd5(p >> 1, q >> 1) << 1)
 
    # a is odd, b is even
    if ((~q & 1) == 1):
        return gcd5(p, q >> 1)
 
    # reduce larger number
    if (p > q):
        return gcd5((p - q) >> 1, q)
 
    return gcd5((q - p) >> 1, p)

if __name__ == "__main__":
    # python -m doctest -v 000_gcd.py
    doctest.testmod()