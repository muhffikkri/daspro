# Nama File : garis.py
# Deskripsi : membuat tipe bentukan garis beserta konstruksi dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 11 Oktober 2024


from math import sqrt

def absis (P) :
    return P[0]

def ordinat (P) :
    return P[1]

def garisAwal (P) :
    return P[0]

def garisAkhir (P) :
    return P[1]

def makePoint (a, b):
    return [a, b]

def makeGaris (P1, P2) : 
    return [P1, P2]

def Gradien (G) :   
    return (ordinat(garisAkhir(G)) - ordinat(garisAwal(G))) / (absis(garisAkhir(G)) - absis(garisAwal(G)))

def PanjangGaris (G):
    return sqrt(
        fx2(absis(garisAkhir(G)) - absis(garisAwal(G))) + 
        fx2(ordinat(garisAkhir(G)) - ordinat(garisAwal(G)))
    )

def fx2 (x):
    return x*x

def IsSejajar (G1, G2) : 
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus (G1, G2) :
    return Gradien(G1) * Gradien(G2) == -1


# APLIKASI

p1 = makePoint(4.0, 2.0)
p2 = makePoint(5.0, 4.0)
p3 = makePoint(-4.0, 2.0)
p4 = makePoint(-8.0, 4.0)
g1 = makeGaris(p1, p2)
g2 = makeGaris(p3, p4)
print(Gradien(g1))  # 2.0
print(Gradien(g2))  # -0.5
print(IsSejajar(g1, g2))    # False
print(IsTegakLurus(g1, g2)) # True