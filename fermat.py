#!/usr/bin/python
from math import sqrt, ceil
import sys

def is_perfect_square(n):
    return not (sqrt(n)-int(sqrt(n)))

def fermat_factorization(n):
    x = int(ceil(sqrt(n)))
    r = x**2 - n
    print "Try to find prime factors of", n

    while not is_perfect_square(r):
        print "x =", x, "| r = x^2 - n =", r, "| 2x + 1 = ", 2*x+1
        x = x + 1
        r = x**2 - n

    print "x =", x, "| r = x^2 - n =", r, "| 2x + 1 = ", 2*x+1
    y = int(sqrt(r))
    a = x + y
    b = x - y
    print "Prime factors =>", a, b
    if a == 1 or b == 1:
        print "=>", n, "is prime!"
    return a, b

n = int(sys.argv[1])
fermat_factorization(n)
