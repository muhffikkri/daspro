# Nama File : latihanA.py
# Deskripsi : membuat fungsi rekursif
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 01 Oktober 2024

def faktorial(n) :
    return 1 if n == 1 else n * faktorial(n - 1)

def fibonacci(n) : 
    if n == 0: return 0
    elif n == 1: return 1
    else : return n + fibonacci(n - 1) 

def tambah(x, y) : 
    return x if y == 0 else tambah(x, y - 1) + 1

def kurang(x, y) : 
    return x if y == 0 else kurang(x, y - 1) - 1

def bagi(x, y) : 
    return 0 if x < y else 1 + bagi(x - y, y)

def pangkat(x, y) : 
    return 1 if y == 0 else x * pangkat(x, y - 1)

def kali(x, y) :
    if y == 0 : return 0 
    elif y == 1 : return x
    else : return x + kali(x, y - 1)

print(faktorial(5))
print(fibonacci(5))
print(tambah(5,5))
print(kurang(5,5))
print(bagi(5,5))
print(pangkat(5,3))
print(kali(5,5))