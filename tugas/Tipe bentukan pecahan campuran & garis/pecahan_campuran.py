# Nama File : pecahan_campuran.py
# Deskripsi : membuat tipe bentukan pecahan campuran beserta konstruktor dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 11 Oktober 2024


# DEFINISI DAN SPESIFIKASI TYPE

# type pecahanc : <bil: integer, n:integer >= 0, d:integer > 0>
# {<bil, n, d> adalah sebuah pecahan campuran, dengan bil sebagai bilangan bulat, n adalah pembilang (nominator), dan d adalah penyebut (denominator). pembilang selalu lebih kecil dari penyebut (n < d)}

# type pecahan : <n: integer >= 0, d: integer > 0>
# {<n, d> adalah sebuah pecahan biasa, dengan n sebagai pembilang (numerator) dan d sebagai penyebut (denumerator). tipe ini akan menjadi output dari fungsi operator}


# DEFINISI DAN SPESIFIKASI SELEKTOR
# bil: pecahanc --> integer
# {bil (P) mengembalikan komponen ke-0 dari P yaitu bilangan bulat}
# Realisasi fungsi bil
def bil (P) :
    return P[0]

# num: pecahanc --> integer >= 0
# {num (P) mengembalikan komponen ke-1 dari P yaitu pembilang}
def num (P) :
    return P[1]

# denum: pecahanc --> integer > 0
# {denum (P) mengembalikan komponen ke-2 dari P yaitu penyebut}
# Realisasi fungsi denum
def denum (P) :
    return P[2]


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakePecahanc: 3 integer --> pecahanc
# {MakePecahanc (b, n, d) membentuk sebuah pecahan campuran dari b, n, dan d dengan bil sebagai bilangan bulat, n sebagai pembilang dan d sebagai penyebut}
# Realisasi fungsi MakePecahanc
def MakePecahanc (b, n, d) :
    return [b, n, d]


# MakePecahan: 2 integer --> pecahan
# {MakePecahan (n, d) membentuk sebuah pecahan biasa dari n dan d dengan n sebagai pembilang dan d sebagai penyebut}
# Realisasi fungsi MakePecahan
def MakePecahan (n, d) :
    return [n, d]
# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP PECAHANC

# KonversiPecahan: pecahanc --> pecahan
# {KonversiPecahan (P) mengubah pecahan campuran P ke tipe pecahan biasa}
# Realisasi fungsi KonversiPecahan
def KonversiPecahan (P) :
    return MakePecahan(
            bil(P) * denum(P) + num(P), denum(P)
        )

# KonversiReal : pecahanc --> real
# {KonversiReal (P) mengubah pecahan campuran P ke nilai real}
# Realisasi fungsi KonversiReal
def KonversiReal (P) :
    return numc(P) / denum(P)

# AddP: 2 pecahanc --> pecahanc
# {AddP (P1,P2) menjumlahkan dua buah pecahan campuran P1 dan P2}
# Realisasi fungsi AddP
def AddP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) // (denum(P1) * denum(P2)),
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) - ((denum(P1) * denum(P2)) * 
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )
   
# SubP: 2 pecahanc --> pecahanc
# {SubP (P1,P2) mmengurangkan dua buah pecahan campuran P1 dan P2}
# Realisasi fungsi SubP
def SubP (P1, P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) // (denum(P1) * denum(P2)),
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) - ((denum(P1) * denum(P2)) * 
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )
   
# DivP : 2 pecahanc --> pecahanc
# {DivP (P1,P2) membagi dua buah pecahan campuran P1 dan P2}
# Realisasi fungsi DivP
def DivP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2)) // (denum(P1) * numc(P2)),
        (numc(P1) * denum(P2)) - (denum(P1) * numc(P2)) * 
        ((numc(P1) * denum(P2)) // (denum(P1) * numc(P2))),
        (denum(P1) * numc(P2))
    ) 
# MulP : 2 pecahanc --> pecahanc
# {MulP (P1,P2) mengalikan dua buah pecahan campuran P1 dan P2}
# Realisasi fungsi MulP
def MulP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * numc(P2)) // (denum(P1) * denum(P2)),
        (numc(P1) * numc(P2)) - (denum(P1) * denum(P2)) * 
        ((numc(P1) * numc(P2)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )

# numc : pecahanc --> integer
# {numc (P) mengembalikan pembilang pecahan campuran dari hasil kali antara bilangan bulat dengan denominator kemudian ditambahkan dengan numerator}
# Realisasi fungsi numc
def numc (P) :
    return bil(P) * denum(P) + num(P)


# DEFINISI DAN SPESIFIKASI PREDIKAT

# IsEqP : 2 pecahanc --> boolean
# {IsEqP (P1,P2) membandingkan dua buah pecahan campuran apakah nilai P1 sama dengan P2}
# Realisasi fungsi IsEqP
def IsEqP (P1,P2) :
    return numc(P1) * denum(P2) == numc(P2) * denum(P1)
   
# IsLtP : 2 pecahanc --> boolean
# {IsLtP (P1,P2) membandingkan dua buah pecahan campuran apakah nilai P1 lebih kecil dari P2}
# Realisasi fungsi IsLtP
def IsLtP (P1,P2) :
    return numc(P1) * denum(P2) < numc(P2) * denum(P1)
   




# IsGtP : 2 pecahanc --> boolean
# {IsGtP (P1,P2) membandingkan dua buah pecahan campuran apakah nilai P1 lebih besar dari P2}
# Realisasi fungsi IsGtP
def IsGtP (P1,P2) :
   return numc(P1) * denum(P2) > numc(P2) * denum(P1)


# APLIKASI

P1 = MakePecahanc(2, 1, 2)
P2 = MakePecahanc(1, 1, 2)
print(KonversiPecahan(P1))  # [5, 2]
print(KonversiPecahan(P2))  # [3, 2]
print(KonversiReal(P1))     # 2.5
print(KonversiReal(P2))     # 1.5
print(AddP(P1, P2))     # [4, 0, 4]
print(SubP(P1, P2))     # [1, 0, 4]
print(DivP(P1, P2))     # [1, 4, 6]
print(MulP(P1, P2))     # [3, 3, 4]
print(IsEqP(P1, P2))    # False
print(IsLtP(P1, P2))    # False
print(IsGtP(P1, P2))    # True