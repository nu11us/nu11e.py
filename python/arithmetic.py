def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)


def nCr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


def nPr(n, r):
    return factorial(n)//factorial(n-r)


def collatz_cycles(x):
    if x == 1:
        return 0
    else:
        if x % 2 == 0:
            return 1 + colllength(x//2)
        else:
            return 1 + colllength(3*x + 1)
