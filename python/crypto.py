import string

def string_value(x):
    alphabet = string.ascii_lowercase
    return sum([alphabet.index(i)+1 for i in x.lower()])
    
def rot_shift(text, n):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[n:] + alphabet[:n]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def perm(n, key):
    num = ""
    m = 1
    while True:
        num = str(n%m) + num
        n=(n//m)
        m+=1
        if n==0:
            break
    tup2 = [0]*len(key)
    tup2[0] = key[int(num[0])]
    key.pop(int(num[0]))
    for i,j in enumerate(num[1:]):
        tup2[i+1] = key[int(j)]
        key.pop(int(j))
    return tup2