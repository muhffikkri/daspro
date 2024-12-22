# Nama File : point.py
# Deskripsi : membuat tipe bentukan point beserta konstruksi dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 24 September 2024

from math import sqrt

# DEFINISI DAN SPESIFIKASI FUNGSI FX2
# fx2: integer --> integer
# {fx2(x) menghitung hasil pangkat 2 dari x}
# Realisasi dalam Python
def fx2(x):
    return x*x

# DEFINISI TYPE
# type point : <x:real, y:real>
# {<x, y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real --> point
# {MakePoint(x, y) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat} 
# Realisasi dalam Python
def makePoint(a, b):
    return [a, b]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis: point --> real
# {Absis(P) memberikan absis point P}
# Realisasi dalam Python
def absis(P):
    return P[0]

# Ordinat: point --> real
# {Ordinat(P) memberikan ordinat point P}
# Realisasi dalam Python
def ordinat(P):
    return P[1]

# InfoPoint: point --> string
# {InfoPoint(P) memberikan informasi absis dan ordinat P}
# Realisasi dalam Python
def infoPoint(P):
    return f"Absis: {absis(P)}, Ordinat: {ordinat(P)}"

# DEFINISI DAN SPESIFIKASI OPERATOR
# Jarak: 2 point --> real
# {Jarak(P1, P2) menghitung jarak antara 2 point P1 dan P2}
# Realisasi dalam Python
def jarak(P1, P2):
    return sqrt(
        fx2(absis(P2) - absis(P1)) + 
        fx2(ordinat(P2) - ordinat(P1))
    )

# JarakO: point --> real
# {JarakO(P) menghitung jarak antara P dengan titik origin (0, 0)}
# Realisasi dalam Python
def jarakO(P):
    return sqrt(
        fx2(absis(P) + ordinat(P))
    )

# Kuadran: point --> string
# {Kuadran(P) mengembalikan kuadran di mana point P berada, dengan syarat P bukan titik (0, 0) tidak terletak di sumbu X maupun sumbu Y}
# Realisasi dalam Python 
def kuadran(P):
    if(absis(P) > 0) : return "Kuadran 1" if ordinat(P) > 0 else "Kuadran 4"
    return "Kuadran 2" if ordinat(P) > 0 else "Kuadran 3"

# APLIKASI
P = makePoint (1,2)
Q = makePoint (4,6)
print(absis(P)) # --> 1
print(ordinat(P)) # --> 2
print(infoPoint(P)) # --> "Absis: 1, Ordinat: 2"
print(jarak(P,Q)) # --> 5.0
print(jarakO(P)) # --> 3.0
print(kuadran(P)) # --> "Kuadran 1"