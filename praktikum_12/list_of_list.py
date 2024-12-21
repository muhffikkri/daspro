from list import *

# Nama File : list.py
# Deskripsi : berisi type dan operasi list
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 29 Oktober 2024

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

# IsEqual : 2 List -> boolean 
# {IsEqual(L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan sama nilainya}
def IsEqual(L1,L2):
    if(IsEmpty(L1) and IsEmpty(L2)):
        return True
    else:
        if(FirstElmt(L1) == FirstElmt(L2)):
            return IsEqual(Tail(L1),Tail(L2))
        else:
            return False

# IsMemberLS: list, list of list-> boolean  
# IsMemberLS(L,S) mengembalikan true jika list L ada di dalam list of list S  
def IsMemberLS(L,S): 
    if(IsEmpty (S)): 
        return False 
    else: 
        if(IsAtom (FirstList(S))): 
            return IsMemberLS (L, TailList(S)) 
        else: 
            if (IsEqual(FirstList(S), L)): 
                return True 
            else: 
                return IsMemberLS (L, TailList(S))
            
# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST  
# IsEgS: 2 list of list -> boolean 
# IsEqS(51,52) benar jika Si memiliki elemen dengan nilai dan urutan yang sama dengan S2 
def isEqS(S1,S2): 
    if(IsEmpty (S1) and IsEmpty (S2)): 
        return True 
    elif(IsEmpty (S1) and not IsEmpty (S2)): 
        return False 
    elif(not IsEmpty (S1) and IsEmpty(S2)): 
        return False 
    else: 
        if(IsAtom(FirstList(S1)) and IsAtom(FirstList(S2))): 
            if(FirstList(S1) == FirstList(S2)): 
                return isEqS(TailList(S1), TailList(S2)) 
            else: 
                return False
        elif(IsList(FirstList(S1)) and IsList(FirstList(S2))): 
            return isEqS(FirstList(S1), FirstList(S2)) and isEqS(TailList(S1), TailList(S2)) 
        else: 
            return False 

# IsMemberS: elemen, list of list-> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
def IsMemberS(x, S) : 
    if IsEmpty(S) : 
        return False
    else : 
        if IsAtom(FirstElmt(S)) :
            if x == FirstElmt(S) :
                return True
            else : 
                return IsMemberS(x, TailList(S)) 
        else : 
            return IsMemberS(x, FirstElmt(S)) or IsMemberS(x, TailList(S))
# Contoh aplikasi:
# print(IsMemberS(3, []))
# print(IsMemberS(3, [2, 4, 3, [1], [4,5]]))
# print(IsMemberS(3, [2, 4, 7, [1], [3,5]]))

# Rember: elemen, list of list -> list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
def Rember(e, S) : 
    if IsEmpty(S) : 
        return []
    else : 
        if IsAtom(FirstElmt(S)) :
            if e == FirstElmt(S) :
                return Rember(e, TailList(S))
            else : 
                return KonsLo(FirstElmt(S), Rember(e, TailList(S)))
        else : 
            if e == FirstElmt(S) :
                return Rember(e, TailList(S))
            else : 
                return KonsLo(Rember(e, FirstElmt(S)), Rember(e, TailList(S)))
# Contoh aplikasi:
# print(Rember(3, [])) 
# print(Rember(3, [4, 3, [2,4], 3])) 
# print(Rember(3, [2, 4, [3,6,9], 5, 3])) 

# max2: 2 real -> real
# max2(x, y) mengembalikan angka terbesar dari x atau y
def max2(x, y) : 
    return x if (x > y) else y

def Max(S) :
    if IsEmpty(S) :
        return 0
    else : 
        if IsAtom(FirstList(S)) :
            return max2(FirstList(S), Max(TailList(S)))
        else :
            return max2(Max(FirstList(S)), Max(TailList(S)))
# Contoh aplikasi:
# print(Max([4, 5, 6, [8,9,10], [12,0], 8]))
# print(Max([4, 15, 6, [8,9,10], [12,0], 8]))

# NBElmtAtom: list of list -> integer
# NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
def NBElmtAtom(S) : 
    if IsEmpty(S) : 
        return 0
    else : 
        if IsAtom(FirstElmt(S)) :
            return 1 + NBElmtAtom(TailList(S))
        else : 
            return NBElmtAtom(TailList(S))
# Contoh aplikasi:
# print(NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8]))
# print(NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8]))
# print(NBElmtAtom([[8,9,10]]))

# NBElmtList: list of list -> integer
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
def NBElmtList(S) : 
    if IsEmpty(S) : 
        return 0
    else : 
        if IsList(FirstElmt(S)) : 
            return 1 + NBElmtList(TailList(S))
        else : 
            return NBElmtList(TailList(S))
# Contoh aplikasi:
# print(NBElmtList([4, 5, 6, [8,9,10], [12,0], 8])) 
# print(NBElmtList([[4, 15], 6, [8,9], 10, [12], 8])) 
# print(NBElmtList([[8,9,10]])) 

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
# print(SumLol([4, 5, 6, [2,3,1]]))
# print(SumLol([[2,3,4]]))

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
# print(MaxNBElmtList([[4,5,6,7], [12], 12, [8,9,10], [12,0], 8]))
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


def max2(a, b) :
    if a > b :
        return a
    else :
        return b
    
# Contoh aplikasi:
# print(MaxSumElmt([[1,2], 9, [4,5,6], 8]))
# print(MaxSumElmt([[1,2], 90, [4,5,6], 8]))
# print(MaxSumElmt([8,9,10]))
# print(MaxSumElmt([[8,9,10]]))
