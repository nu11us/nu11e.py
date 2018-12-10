import string

def string_value(x):
    alphabet = string.ascii_lowercase
    return sum([alphabet.index(i)+1 for i in x.lower()])
    
def rot_shift(text, n):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[n:] + alphabet[:n]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)
