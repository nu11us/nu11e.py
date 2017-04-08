 """             
| \ | |     | | |                   
|  \| |_   _| | | ___   _ __  _   _ 
| . ` | | | | | |/ _ \ | '_ \| | | |
| |\  | |_| | | |  __/_| |_) | |_| |
\_| \_/\__,_|_|_|\___(_) .__/ \__, |
                       | |     __/ |
                       |_|    |___/ 

A personal number theory library.
- nu11us, MIT License
"""
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)

def log(a, n):
    if n%a == 0:
        return 1 + log(a, n//a)
    else:
        return 0 

def nCr(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

def nPr(n,r):
    return factorial(n)//factorial(n-r)

def nelattice_path(n,e):
    return nCr(n+e, e)
	
def divisor_list(x):
    st = []
    for y in range(1,x):
        if x%y == 0:
            if y in st:
                break;
            st.append(y)
            st.append(x//y)
    return sorted(st)

def string_value(x):
    dicti = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    x   = x.lower()
    mx  = 0
    for i in x:
        mx += dicti[i]
    return mx

def collatz_cycles(x):
    if x==1:
        return 0
    else:
        if x%2 == 0:
            return 1 + colllength(x//2)
        else:
            return 1 + colllength(3*x +1)

def primes_erat(lim):
    x   = [0]*2 + [1]*(lim-2)
    lst = []
    for (i,prime) in enumerate(x):
        if prime:
          lst.append(i)
          for j in range(i*2, lim, i):
            x[j] = 0
    return lst