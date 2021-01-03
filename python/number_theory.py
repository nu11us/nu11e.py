import math
from Decimal import *

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
