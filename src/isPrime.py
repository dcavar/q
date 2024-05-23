#!/usr/bin/env python3

"""
testPrime.py
(C) 2018 by Damir Cavar <damir@cavar.me>

Testing for prime number, based on the pseudo-code on the Wikipedia page:

https://en.wikipedia.org/wiki/Primality_test

"""


def isPrime(n):
    """
    """

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    print("3:", isPrime(3))
    print("42:", isPrime(42))
    print("17:", isPrime(17))


