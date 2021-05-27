import math
#from Decimal import *

def primes_erat(lim):
    x = [0]*2 + [1]*(lim-2)
    s = set()
    for (i, prime) in enumerate(x):
        if prime:
            s.add(i)
            for j in range(i*2, lim, i):
                x[j] = 0
    return s

def triangle(x):
    return x*(x + 1) // 2

def pentagon(x):
    return x*(3*x - 1) // 2

def partition(n):
    if n == 0:
        return 1
    s = 0
    for k in range(1, n+1):
        s += ((-1)**(k-1))*(partition(n-pentagon(k))+partition(n-pentagon(-k)))
    return s

def extended_euclid(a,b):
    r0, r = a, b
    s0, s = 1, 0
    t0, t = 0, 1
    while r != 0:
        q = r0 // r
        r0, r = r, r0 - q*r
        s0, s = s, s0 - q*s
        t0, t = t, t0 - q*t
    return (s0, t0)

def modinv(a,b):
    if math.gcd(a,b) != 1:
        return None
    x, y = extended_euclid(a,b)
    if x < 0:
        x = (x % b + b) % b
    return x

def crt(a1, a2, n1, n2):
    x,y = extended_euclid(n1,n2)
    m = n1*n2
    n = a2*x*n1 + a1*y*n2
    return (n % m + m) % m

def crt_full(lst):
    while len(lst) > 1:
        tup1 = lst[0]
        tup2 = lst[1]
        a = crt(lst[0][0],lst[1][0],lst[0][1],lst[1][1]) 
        n = lst[0][1]*lst[1][1]
        lst[0] = (a,n)
        lst.pop(1)
    return lst[0][0]

def chakravala_pell(n):
    getcontext().prec = 40
    a = Decimal(8)
    b = Decimal(1)
    k = Decimal(a**2 - n*b**2)
    while True:
        if k == 1:
            getcontext().prec = 28
            return (int(a),int(b))

        z = max([100, n])
        lst = []
        for m in range(z):
            if ((a + b*m) / k) % 1 == 0:
                lst.append((abs((m**2 - n) / k),m))
        m = sorted(lst)[0][1]
        a,b,k = (a*m + n*b)/abs(k), (a + b*m)/abs(k), (m**2 - n)/k

def gen_pyth_triples(bound=800000):
    dictionary = {}
    b = int(sqrt(bound))
    y = set()
    z = []
    d = {}
    for i in range(1, b):
        for j in range(i+1, b):
            if (i + j) % 2 == 1:
                if gcd(i, j) == 1:
                    x = j + (i+j)*(i+j+1)//2
                    y.add(x)
                    d[x] = (i,j)
    for d_i in d:
        if d_i * d[d_i][0] % d[d_i][1] == 0:
            b = int(d_i * d[d_i][0] / d[d_i][1])
        else:
            b = 2*d[d_i][1]*d[d_i][1] - (d[d_i][0]**2 + d[d_i][1]**2)
        c = d[d_i][0]**2 + d[d_i][1]**2
        a = int(sqrt(c**2 - b**2))
        z.append((a,b,c))
    return z

def pell(d):
    y = 1
    while True:
        if (math.sqrt(d*y*y + 1)) % 1 < 1e-9:
            if int(math.sqrt(d*y*y + 1))**2 - d*y*y == 1:
                return (math.sqrt(d*y*y + 1),y)
        else:
            y += 1
