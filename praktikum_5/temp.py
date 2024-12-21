from list_of_list import *

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST 
# IsEmpty: list of list -> boolean 
# IsEmpty(S) benar jika S adalah list of list kosong. 
def IsEmpty(L): 
    return L == [] 

# IsAtom: list of list -> boolean 
# IsAtom(S) benar jika S adalah sebuah atom. 
def IsAtom(S): 
    return type(S) != list 

# IsList: list of list -> boolean 
# IsList(S) benar jika S adalah sebuah list. 
def IsList(S): 
    return type(S) == list

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR  
# KonsLo: list, list of list -> list of list 
# KonsLo(L,S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (s). 
def KonsLo(L,S):  
    return [L] + S  

# Konsti: list of list, list -> list of list  
# KonsLi(S,L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S). 
def KonsLi(S,L):  
    return S + [L]

# DEFINISI DAN SPESIFIKASI SELEKTOR 
# FirstList: list of list tidak kosong -> list 
# FirstList(S) menghasilkan elemen pertama list (mungkin sebuah list atau atom) 
def FirstList(S):  
    return S[0] 

# LastList: list of list tidak kosong -> list 
# LastList(S) menghasilkan elemen terakhir list (mungkin sebuah list atau atom) 
def LastList(S): 
    return S[-1]

# TailList: list of list tidak kosong -> list of list  
# LastList(S) menghasilkan sisa list of list S tanpa elemen pertamanya. 
def TailList(S):   
    return S[1:] 

# HeadList: list of list tidak kosong -> list of list 
# HeadList(S) menghasilkan sisa list of list S tanpa elemen terakhirnya. 
def HeadList(S): 
    return S[:-1]

# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# max2: 2 real -> real
# max2(x, y) mengembalikan angka terbesar dari x atau y
def max2(x, y) : 
    return x if (x > y) else y

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
def SumLol(S) : 
    if IsEmpty(S) : 
        return 0
    else : 
        if IsAtom(FirstList(S)) :
            return FirstList(S) + SumLol(TailList(S))
        else : 
            return SumLol(FirstList(S)) + SumLol(TailList(S))
# Contoh aplikasi:
# print(SumLol([[]]))
# print(SumLol([1,2,4,[9,6,4],[2,1]]))
# print(SumLol([[4,5]]))

# MaxNBElmtList: list of list -> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
def MaxNBElmtList(S) :
    if IsEmpty(S) : 
        return 0
    else : 
        if IsList(FirstList(S)) : 
            return max2(NBElmtAtom(FirstList(S)), MaxNBElmtList(TailList(S)))
        else : 
            return MaxNBElmtList(TailList(S))
# Contoh aplikasi:
# print(MaxNBElmtList([[1,2,3,4,5],1,2,[1,2],[3,5,2]]))
# print(MaxNBElmtList([[4,15], 6, [8,9], 10, [12], 8]))
# print(MaxNBElmtList([8,9,10, 10]))

# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
# jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut
# jika elemen atom, maka nilainya adalah elemen tersebut
def MaxSumElmt(S) :
    if IsEmpty(S) :
        return 0
    else : 
        if IsAtom(FirstList(S)) : 
            return max2(FirstList(S), MaxSumElmt(TailList(S)))
        else : 
            return max2(SumElmt(FirstList(S)), MaxSumElmt(TailList(S)))
# Contoh aplikasi:
print(MaxSumElmt([1,2,3,[12,2,3,3],14,5]))
print(MaxSumElmt([5,7,50,[12,2,3,1],4,5]))
print(MaxSumElmt([6,7,1,[2,4,5,6],1,3,6]))

def SumLol(S) : 
    if IsEmpty(S) : 
        return 0
    else : 
        if IsAtom(FirstList(S)) :
            return FirstList(S) + SumLol(TailList(S))
        else : 
            return SumLol(FirstList(S)) + SumLol(TailList(S))

def MaxNBElmtList(S) :
    if IsEmpty(S) : 
        return 0
    else : 
        if IsList(FirstList(S)) : 
            return max2(NBElmtAtom(FirstList(S)), MaxNBElmtList(TailList(S)))
        else : 
            return MaxNBElmtList(TailList(S))            
        
def MaxSumElmt(S) :
    if IsEmpty(S) :
        return 0
    else : 
        if IsAtom(FirstList(S)) : 
            return max2(FirstList(S), MaxSumElmt(TailList(S)))
        else : 
            return max2(SumElmt(FirstList(S)), MaxSumElmt(TailList(S)))