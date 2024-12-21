# Nama File : pecahan_campuran.py
# Deskripsi : membuat tipe bentukan pecahan campuran beserta konstruktor dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 11 Oktober 2024

# DEFINISI TYPE
# type pecahanc : <bil: integer, n:integer >= 0, d:integer > 0 >
# {<bil, n, d> adalah sebuah pecahan campuran, dengan bil sebagai bilangan bulat, n adalah pembilang (nominator), dan d adalah penyebut (denominator). pembilang selalu lebih kecil dari penyebut (n < d)}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makePecahan: 3 integer --> pecahanc
# makePecahan(n, a,b) membentuk sebuah array dari a dan b dengan a sebagai pembilang dan b sebagai penyebut}
# Realisasi fungsi makePecahan
def makePecahan (bil, n,d) :
    return [bil, n, d]
   
# pemb: pecahan --> real
# {pemb (P) mengembalikan komponen array ke-0 dari P}
# Realisasi fungsi pemb
def pemb (P) :
    return P[0]
   
# pemb: pecahan --> real
# {pemb (P) mengembalikan komponen array ke-1 dari P}
# Realisasi fungsi peny
def peny (P) :
    return P[1]
   
# AddP: 2 pecahan --> pecahan
# {AddP (P1,P2) menjumlahkan dua buah pecahan P1 dan P2}
# Realisasi fungsi AddP
def AddP (P1,P2) :
    return makePecahan(
            (pemb(P1) * peny(P2)) + (pemb(P2) * peny(P1)), 
            peny(P1) * peny(P2)
        )
   
# SubP: 2 pecahan --> pecahan
# {SubP (P1,P2) mmengurangkan dua buah pecahan P1 dan P2}
# Realisasi fungsi SubP
def SubP (P1, P2) :
    return makePecahan(
            (pemb(P1) * peny(P2)) - (pemb(P2) * peny(P1)), 
            peny(P1) * peny(P2)
    )
   
# MulP : 2 pecahan --> pecahan
# {MulP (P1,P2) mengalikan dua buah pecahan P1 dan P2}
# Realisasi fungsi MulP
def MulP (P1,P2) :
    return makePecahan(
        pemb(P1) * pemb(P2),
        peny(P2) * peny(P2)
    )
   
# DivP : 2 pecahan --> pecahan
# {DivP (P1,P2) membagi dua buah pecahan P1 dan P2}
# Realisasi fungsi DivP
def DivP (P1,P2) :
    return makePecahan(
        pemb(P1) * peny(P2),
        pemb(P2) * peny(P1)
    )
   
# REalP : 1 pecahan --> real
# {REalP (P) menuliskan pecahan dalam bentuk notasi desimal}
# Realisasi fungsi RealP
def RealP (P) :
    return pemb(P)/peny(P)
   
# IsEqP : 2 pecahan --> boolean
# {IsEqP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 sama dengan P2}
# Realisasi fungsi IsEqP
def IsEqP (P1,P2) :
    return pemb(P1) == pemb(P2) and peny(P1) == peny(P2)
   
# IsLtP : 2 pecahan --> boolean
# {IsLtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih kecil P2}
# Realisasi fungsi IsLtP
def IsLtP (P1,P2) :
    return True if(pemb(P1) * peny(P2) < pemb(P2) * peny(P1)) else False
   
# IsGtP : 2 pecahan --> boolean
# {IsGtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih besar P2}
# Realisasi fungsi IsGtP
def IsGtP (P1,P2) :
   return True if(pemb(P1) * peny(P2) > pemb(P2) * peny(P1)) else False

#APLIKASI
P = makePecahan (1,2)
Q = makePecahan (1,2)
print (pemb(P)) # --> 1
print (peny(P)) # --> 2
print (AddP (P,Q)) # --> [4, 4]
print (SubP (P,Q)) # --> [0, 4]
print (MulP (P,Q)) # --> [1, 4]
print (DivP (P,Q)) # --> [2, 2]
print (RealP (P)) # --> 0.5
print (IsEqP (P,Q)) # --> True
print (IsLtP (P,Q)) # --> False
print (IsGtP (P,Q)) # --> False