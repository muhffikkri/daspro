from list import *
from list_of_list import *

# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
def MakePB(A, L, R):
    return [A, L, R]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2] 

# IsTreeEmpty : PohonBiner → boolean
# {IsTreeEmpty(P) true jika P kosong : (// \\) }
def IsTreeEmpty(T):
    return T == []

# IsOneElmt : PohonBiner → boolean
# {IsOneElement(P) true jika P hanya mempunyai satu elemen, yaitu akar (// A \\\) } 
def IsOneElmt(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))

# IsUnerLeft : PohonBiner → boolean
# {IsUnerLeft(P) true jika P hanya mengandung sub pohon kiri tidak kosong: (//L A \\) } 
def IsUnerLeft(T) :
    return (not IsTreeEmpty(Left(T))) and (IsTreeEmpty(Right(T)))

# IsUnerRight : PohonBiner → boolean
# {IsUnerRight (P) true jika P hanya mengandung sub pohon kanan tidak kosong: (//A R\\) }
def IsUnerRight(T) :
    return (IsTreeEmpty(Left(T))) and (not IsTreeEmpty(Right(T)))

# IsBiner : PohonBiner tidak kosong → boolean
# {IsBiner(P) true jika P mengandung sub pohon kiri dan sub pohon kanan : 
# (//L A R\\) } 
def IsBiner(T) :
    return (not IsTreeEmpty(Left(T))) and (not IsTreeEmpty(Right(T)))

# IsExistLeft : PohonBiner tidak kosong → boolean
# {IsExistLeft (P) true jika P mengandung sub pohon kiri }
def IsExistLeft(T) :
    return (not IsTreeEmpty(Left(T)))

# IsExistRight : PohonBiner tidak kosong → boolean
#  {ExistRight(P) true jika P mengandung sub pohon kanan }
def IsExistRight(T) :
    return (not IsTreeEmpty(Right(T)))
    

def PrintBinaryTreeHelp(T, indent):
    if T != []:
        print(indent + str(Akar(T)))
        PrintBinaryTreeHelp(Left(T), indent + '\t')
        PrintBinaryTreeHelp(Right(T), indent + '\t')
    else:
        print(indent + "[]")

def PrintBinaryTree(T):
    PrintBinaryTreeHelp(T, '')

# NbElmt : PohonBiner → integer ≥ 0
#  {NbElmt(P) memberikan Banyaknya elemen dari pohon P :
#  Basis : NbElmt (//A\ \) = 1
#  Rekurens : NbElmt (//L,A,R\\ ) = NbElmt(L) + 1 + NbELmt(R)
#  NbElmt (//L,A,\ ) = NbElmt(L) + 1
#  NbElmt (//A,R\\ ) = 1 + NbELmt(R) } 
def NbElmtTree(T):
    if IsTreeEmpty(T):
        return 0
    else:
        return NbElmtTree(Left(T)) + 1 + NbElmtTree(Right(T))

# NbDaun : PohonBiner → integer ≥ 0
# { definisi : Pohon kosong berdaun 0 }
# {NbDaun (P) memberikan Banyaknya daun dari pohon P :
# Basis-1 : NbDaun (//\ \) = 0
# Rekurens :
# NbDaun1 (P) 
def NbDaun(T) :
    if IsTreeEmpty(T):
        return 0
    elif IsOneElmt(T) :
        print(Akar(T))
        return 1
    # elif (not IsEmpty(Left(T))) and (IsEmpty(Right(T))) :
    #     return NbDaun(Left(T))
    # elif (IsEmpty(Left(T))) and (not IsEmpty(Right(T))) :
    #     return NbDaun(Right(T))
    else : 
        return NbDaun(Left(T)) + NbDaun(Right(T))

# NbDaun1 : PohonBiner → integer ≥ 1
# { Prekondisi : Pohon P tidak kosong }
# {NbDaun (P) memberikan Banyaknya daun dari pohon P :
# Basis : NbDaun1 (//A\ \) = 1
# Rekurens : NbDaun1 (//L,A,R\\) = NbDaun1 (L) + NbDaun1(R)
# NbDaun1 (//L,A,\\) = NbDaun1 (L)
# NbDaun1 (//A,R\\) = NbDaun1 (R)     
def NbDaun1(T) :
    if IsOneElmt(T) :
        print(Akar(T))
        return 1
    if ((not IsEmpty(Left(T))) and (not IsEmpty(Right(T)))): 
        return NbDaun(Left(T)) + NbDaun(Right(T))
    elif (not IsEmpty(Left(T))) and (IsEmpty(Right(T))) :
        return NbDaun(Left(T))
    elif (IsEmpty(Left(T))) and (not IsEmpty(Right(T))) :
        return NbDaun(Right(T))

# BSearchX : BinSearchTree, elemen → boolean
# { BsearchX(P,X) Mengirimkan true jika ada node dari Pohon Binary Search Tree P yang
# bernilai X, mengirimkan false jika tidak ada} 
def BSearchX(T, e) :
    if IsTreeEmpty(T) : 
            return False
    else : 
        if IsOneElmt(T) : 
            if e == Akar(T):
                return True
            else :
                return False
        else :
            if Akar(T) == e : 
                return True        
            else : 
                if IsBiner(T) : 
                    return BSearchX(Left(T), e) or BSearchX(Right(T), e)
                else : 
                    if IsUnerLeft(T) : 
                        return BSearchX(Left(T), e)
                    else : 
                        return BSearchX(Right(T), e)

# DelDaun : PohonBiner tidak kosong, elemen → PohonBiner
# { DelDaun(P,X) dengan X adalah salah satu daun , menghasilkan sebuah pohon tanpa X
# yang semula adalah daun dari P} 
def DelDaun(T, e) : 
    if IsTreeEmpty(T) : 
        return T
    else :
        if IsOneElmt(T) : 
            if Akar(T) == e : 
                return []
            else : 
                return MakePB(Akar(T), [], [])
        else : 
            if IsBiner(T) : 
                return MakePB(Akar(T), DelDaun(Left(T), e), DelDaun(Right(T), e))
            else : 
                if IsUnerLeft(T) : 
                    return MakePB(Akar(T), DelDaun(Left(T), e), [])
                elif IsUnerRight(T) :
                    return MakePB(Akar(T), [], DelDaun(Right(T), e))

# LevelOfX: PohonBiner, elemen → integer
# { LevelOfX(P,X) Mengirimkan level dari node X yang merupakan salah satu simpul dari
# pohon biner P }
def LevelOfX(T, e) : 
    if IsTreeEmpty(T) : 
        return 0     
    else : 
        if BSearchX(T, e) : 
            if IsOneElmt(T) : 
                if Akar(T) == e : 
                    return 1
                else : 
                    return 0
            else :
                if Akar(T) == e : 
                    return 1
                else : 
                    if IsBiner(T) : 
                        return 1 + LevelOfX(Left(T), e) + LevelOfX(Right(T), e)
                    else : 
                        if IsUnerLeft(T) : 
                            return 1 + LevelOfX(Left(T), e)
                        else :
                            return 1 + LevelOfX(Right(T), e)
        else : 
            return 0

# AddDaun : PohonBiner tidak kosong, node,node, boolean → PohonBiner
# {AddDaun (P,X,Y,Kiri) : P bertambah simpulnya, dengan Y sebagai anak kiri X (jika
# Kiri), atau sebagai anak Kanan X (jika not Kiri)
# { Prekondisi : X adalah salah satu daun Pohon Biner P } 
def AddDaun(T, X, Y, Kiri) : 
    if IsOneElmt(T) : 
        if Akar(T) == X : 
            if Kiri : 
                return MakePB(Akar(T), MakePB(Y, [], []), [])
            else : 
                return MakePB(Akar(T), [], MakePB(Y, [], []))
        else : 
            return T
    else : 
        # if Akar(T) == X : 
        #     if Kiri : 
        #         return MakePB(Akar(T), MakePB(Y, [], []), Right(T))
        #     else : 
        #         return MakePB(Akar(T), Left(T), MakePB(Y, [], []))
        # else : 
            if IsBiner(T) : 
                return MakePB(Akar(T), AddDaun(Left(T), X, Y, Kiri), AddDaun(Right(T), X, Y, Kiri))
            else : 
                if IsUnerLeft(T) : 
                    return MakePB(Akar(T), AddDaun(Left(T), X, Y, Kiri), [])
                else : 
                    return MakePB(Akar(T), [], AddDaun(Right(T), X, Y, Kiri))
                

# MakeListDaun : PohonBiner →list Of Node
# {MakeListDaun(P) : }
# {Jika P adalah pohon kosong, maka menghasilkan list kosong.
# {Jika P bukan pohon kosong: menghasilkan list yang elemennya adalah semua daun
# pohon P} 
def MakeListDaun(T) : 
    return MakeListDaunHelper(MakeListDaunTree(T))

# MakeListDaunTree : PohonBiner →list Of Node
# {MakeListDaunTree(P) : }
# {Jika P adalah pohon kosong, maka menghasilkan list kosong.
# {Jika P bukan pohon kosong: menghasilkan list yang elemennya adalah semua daun
# pohon P}
def MakeListDaunTree(T):
    if IsOneElmt(T):
        return [Akar(T)]
    else :
        if IsTreeEmpty(T):
            return []    
        else:
            if IsBiner(T):
                # return KonsLo(MakeListDaunTree(Right(T)), []) + KonsLo(MakeListDaunTree(Left(T)), [])
                return KonsLo(MakeListDaunTree(Right(T)), MakeListDaun(Left(T)))
            else : 
                if IsUnerLeft(T):
                    return KonsLo(MakeListDaunTree(Left(T)), [])
                else : 
                    return KonsLo(MakeListDaunTree(Right(T)), [])

# Assuming the following helper functions are defined elsewhere in the file:
# IsList(T), FirstElmt(T), Tail(T), IsAtom(T), KonsLo(e, T), IsEmpty(T), Akar(T), Left(T), Right(T), MakePB(e, L, R), PrintBinaryTree(T), NbDaun1(T), NbElmtTree(T), NbDaun(T)
def MakeListDaunHelper(T):
    """
    Create a list of leaves from a binary tree.

    :param T: The binary tree.
    :type T: list
    :return: A list of leaves from the binary tree.
    :rtype: list

    :example:
    >>> MakeListDaunHelper(['A', ['B', ['C', [], []], ['D', ['E', [], []], ['F', [], []]]], ['G', ['H', [], []], []]])
    ['C', 'E', 'F', 'H']

    :raises TypeError: If T is not a list.
    """
    if IsEmpty(T):
        return []
    if IsList(FirstElmt(T)):
        return MakeListDaunHelper(FirstElmt(T)) + MakeListDaunHelper(Tail(T))
    else:
        if IsAtom(FirstElmt(T)):
            return KonsLo(FirstElmt(T), MakeListDaunHelper(Tail(T)))
        else:
            return MakeListDaunHelper(Tail(T))

def SearchMaxOdd(T, f):
    """
    Search for the maximum odd value in a binary tree.

    :param T: The binary tree.
    :type T: list
    :param f: A function to check if a value is odd.
    :type f: function
    :return: The maximum odd value in the binary tree.
    :rtype: int

    :example:
    >>> SearchMaxOdd(['A', ['B', ['C', [], []], ['D', ['E', [], []], ['F', [], []]]], ['G', ['H', [], []], []]], lambda x: x % 2 != 0)
    0

    :raises TypeError: If T is not a list or f is not a function.
    """
    if IsEmpty(T):
        return 0
    else:
        if f(Akar(T)):
            return max2(0, max2(SearchMaxOdd(Left(T), f), SearchMaxOdd(Right(T), f)))
        else:
            return max2(Akar(T), max2(SearchMaxOdd(Left(T), f), SearchMaxOdd(Right(T), f)))

if __name__ == "__main__":
    T = MakePB('A', 
            MakePB('B', 
                MakePB('C', [], []), 
                MakePB('D', 
                       MakePB('E', [], []), 
                       MakePB('F', [], [])
                       )
                ),  
            MakePB('G', 
                   MakePB('H', [], []), 
                   []) 
            )
    PrintBinaryTree(T)
    print(T)
    print("Jumlah daun di dalam Tree pake NB1: ", NbDaun1(T))
    print("Jumlah node di dalam Tree: ", NbElmtTree(T))
    print("Jumlah daun di dalam Tree: ", NbDaun(T))

    # Examples for MakeListDaunHelper function
    print(MakeListDaunHelper(T))

    # Examples for SearchMaxOdd function
    print(SearchMaxOdd(T, lambda x: x % 2 != 0))