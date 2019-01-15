from itertools import combinations
from operator import mul
from functools import reduce


def primes_erat(lim):
    x = [0]*2 + [1]*(lim-2)
    lst = []
    for (i, prime) in enumerate(x):
        if prime:
          lst.append(i)
          for j in range(i*2, lim, i):
            x[j] = 0
    return lst


def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)


def nCr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


def nPr(n, r):
    return factorial(n)//factorial(n-r)


def coll(x):
    if x == 1:
        return 0
    else:
        if x % 2 == 0:
            return 1 + coll(x//2)
        else:
            return 1 + coll(3*x + 1)


def pf(n):
    def f(n, primes):
        for i in primes:
            if n % i == 0:
                return [i] + pf(n//i)
        return [n]
    return f(n, primes_erat(n))


def factors(n):
    fac = set()
    fac.add(1)
    fac.add(n)
    pr = pf(n)
    for i in range(1, len(pr)+1):
        for j in combinations(pr, i):
            fac.add(reduce(mul, j, 1))
    return fac
