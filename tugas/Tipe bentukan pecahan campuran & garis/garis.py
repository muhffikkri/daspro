# Nama File : garis.py
# Deskripsi : membuat tipe bentukan garis beserta konstruksi dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 11 Oktober 2024


from math import sqrt

# DEFINISI DAN SPESIFIKASI TYPE

# type point : <x:real, y:real>
# {<x, y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}

# type garis : <P1: point, P2: point>
# {<P1, P2> adalah sebuah garis, dengan P1 adalah titik awal dan P2 adalah titik akhir. Kedua titik ini akan dihubungkan untuk membentuk garis}


# DEFINISI DAN SPESIFIKASI SELEKTOR

# absis: point --> real
# {absis (P) memberikan absis point P}
# Realisasi fungsi absis
def absis (P) :
    return P[0]

# ordinat: point --> real
# {ordinat (P) memberikan ordinat point P}
# Realisasi fungsi ordinat
def ordinat (P) :
    return P[1]

# garisAwal : garis --> point
# {garisAwal (P) memberikan titik awal garis P}
# Realisasi fungsi garisAwal
def garisAwal (P) :
    return P[0]

# garisAkhir : garis --> point
# {garisAkhir (P) memberikan titik akhir garis P}
# Realisasi fungsi garisAkhir
def garisAkhir (P) :
    return P[1]





# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakePoint: 2 real --> point
# {MakePoint (x, y) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat} 
# Realisasi fungsi makePoint
def makePoint (a, b):
    return [a, b]

# MakeGaris: 2 point --> garis
# {MakeGaris (P1, P2) membentuk sebuah garis dari P1 dan P2 dengan P1 sebagai titik awal garis dan P2 sebagai titik akhir garis}
# Realisasi fungsi makeGaris
def makeGaris (P1, P2) : 
    return [P1, P2]


# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP GARIS

# Gradien: garis --> real
# {Gradien (G) mengembalikan nilai gradien dari sebuah garis}
# Realisasi fungsi Gradien
def Gradien (G) :
    return (ordinat(garisAkhir(G)) - ordinat(garisAwal(G))) / (absis(garisAkhir(G)) - absis(garisAwal(G)))

# PanjangGaris: garis --> real
# {PanjangGaris (G) menghitung panjang garis antara 2 point yaitu garis awal dan garis akhir}
# {fungsi antara yang digunakan:  SQRT(x) adalah fungsi dasar untuk menghitung akar pangkat 2 dari x}
# Realisasi fungsi PanjangGaris
def PanjangGaris (G):
    return sqrt(
        fx2(absis(garisAkhir(G)) - absis(garisAwal(G))) + 
        fx2(ordinat(garisAkhir(G)) - ordinat(garisAwal(G)))
    )

# fx2: real --> real
# {fx2(x) menghitung hasil pangkat 2 dari x}
# Realisasi fungsi fx2
def fx2 (x):
    return x*x







# DEFINISI DAN SPESIFIKASI PREDIKAT

# IsSejajar : 2 garis --> boolean
# {IsSejajar (G1, G2) akan mengembalikan nilai true jika G1 sejajar dengan G2. G1 sejajar dengan G2 jika dan hanya jika gradien nya sama}
# Realisasi fungsi IsSejajar 
def IsSejajar (G1, G2) : 
    return Gradien(G1) == Gradien(G2)

# IsTegakLurus : 2 garis --> boolean
# {IsTegakLurus (G1, G2) akan mengembalikan nilai true jika G1 tegak lurus dengan G2. G1 tegak lurus dengan G2 jika dan hanya jika gradien nya menghasilkan -1 ketika dikalikan}
# Realisasi fungsi IsTegakLurus
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