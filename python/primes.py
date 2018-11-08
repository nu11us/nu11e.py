def primes_erat(lim):
    x = [0]*2 + [1]*(lim-2)
    lst = []
    for (i, prime) in enumerate(x):
        if prime:
          lst.append(i)
          for j in range(i*2, lim, i):
            x[j] = 0
    return lst
