# Nama File : set.py
# Deskripsi : berisi type dan operasi set
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 5 November 2024

from list import *

#DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.
def Rember(x,L) :
    if IsEmpty(L) :
        return L
    else : 
        if FirstElmt(L) == x :
            return Tail(L)
        else :
            return Konso(FirstElmt(L), Rember(x, Tail(L)))

# print(Rember(2, [1,2,3,4,5]))

# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.
# List baru yang dihasilkan tidak lagi memiliki elemen x.
# List kosong tetap menjadi list kosong.
def MultiRember(x, L) : 
    if IsEmpty(L) :
        return L
    else : 
        if FirstElmt(L) == x :
            return MultiRember(x, Tail(L))
        else :
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

# print(MultiRember(2, [1,2,3,4,5,2,2]))

#DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
# list kosong tetap menjadi himpunan kosong
def MakeSet(L) : 
    if IsEmpty(L) : 
        return []
    else : 
        if isMember(FirstElmt(L), Tail(L)) : 
            # return Konso(FirstElmt(L), MakeSet(MultiRember(FirstElmt(L), Tail(L))))
            return MakeSet(MultiRember(FirstElmt(L), Tail(L)))
        else : 
            return Konso(FirstElmt(L), MakeSet(Tail(L)))

print(MakeSet([1,2,3,4,5,2,2]))

#DEFINISI DAN SPESIKASI KONSTRUKTOR SET
# KonsoSet: elemen,set -> set
# konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
# dengan syarat e belum ada di dalam himpunan H
def KonsoSet(e, H) : 
    if IsEmpty(H) : 
        return []
    else :
        if isMember(e, H) : 
            return H
        else : 
            return Konso(e, H)
        
# print(KonsoSet(2, [1,2,3,4]))
# print(KonsoSet(2, [1,3,4]))

#DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L) : 
    if IsEmpty(L) : 
        return True

    else : 
        if isMember(FirstElmt(L), Tail(L)) : 
            return False
        else : 
            return IsSet(Tail(L))

# print(IsSet([1,2,3,4,5]))
# print(IsSet([1,2,3,4,5,5,5]))

# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
def IsSubset(H1, H2) : 
    if IsEmpty(H1) : 
        return True
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return IsSubset(Tail(H1), H2)
        else : 
            return False

# print(IsSubset([1,3,5], [1,2,3,4,5]))
# print(IsSubset([1,3,6], [1,2,3,4,5]))

# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2
def IsEqualSet(H1, H2) :
    if NbElmt(H1) != NbElmt(H2) : 
        return False
    else :
        return IsSubset(H1, H2) and IsSubset(H2, H1)

print(IsEqualSet([1,2,3], [1,2,3]))
print(IsEqualSet([1,2,3], [1,2,4]))

# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1, H2) : 
    if IsEmpty(H1) or IsEmpty(H2) : 
        return False
    else : 
        if isMember(FirstElmt(H1), H2) :
            return True 
        else : 
            return IsIntersect(Tail(H1), H2)
    
# print(IsIntersect([3], [3,4,5]))
# print(IsIntersect([1,2,3], [6,4,5]))


#DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2
def MakeIntersect(H1, H2) :
    if IsEmpty(H1) : 
        return []
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else : 
            return MakeIntersect(Tail(H1), H2)

print(MakeIntersect([1,2,3], [3,4,5]))

# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2
def MakeUnion(H1, H2) : 
    if IsEmpty(H1) and IsEmpty(H2) : 
        return []
    elif not IsEmpty(H1) and IsEmpty(H2) : 
        return H1
    elif IsEmpty(H1) and not IsEmpty(H2) : 
        return H2
    else : 
        if isMember(FirstElmt(H1), H2) :
            return MakeUnion(Tail(H1), H2)
        else : 
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))

print(MakeUnion([1,2,3], [4,5,6]))

# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
# tanpa memanfaatkan fungsi MakeIntersect(H1,H2).
def NbIntersect(H1, H2) : 
    if IsEmpty(H1) : 
        return 0
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return 1 + NbIntersect(Tail(H1), H2)
        else : 
            return NbIntersect(Tail(H1), H2)

print(NbIntersect([1,2,3], [3,4,5]))
print(NbIntersect([1,2,3], [3,2,5]))

# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
# tanpa memanfaatkan fungsi MakeUnion(H1,H2).
def NbUnion(H1, H2) : 
    # if not IsEmpty(H1) and IsEmpty(H2) : 
    #     return 0
    # elif IsEmpty(H1) and not IsEmpty(H2) : 
    #     return 0
    if IsEmpty(H1) or IsEmpty(H2) :
        return 0
    else : 
        if isMember(FirstElmt(H1), H2) :
            return 1 + NbUnion(Tail(H1), H2)
        else : 
            return 2 + NbUnion(Tail(H1), H2)
        
print(NbUnion([1,2,3], [3,2,5]))
print(NbUnion([1,2,3], [3,4,5]))
