from treeNaire_24060124130069 import isTreeNEmpty, isOneElmt
def Tail(L) :
    return L[1:]

# Head : List tidak kosong -> List
# Head(L) -> menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi 
def Head(L) :
    return L[:-1]

def IsEmpty(L) :
    return L == []

# ISOneElmt: List -> boolean
# IsOneElmt(X, L) -> adalah benar jika list L hanya mempunyai satu elemen
# Realisasi 
def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

#DEFINISI DAN S PESIFIKASI KONSTRUKTUR
def makePN(A,PN) :
    return [A,PN]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar : PohonN-ner tidak kosong --> Elemen
# Akar(PN) adalah akar dari PN
def Akar(PN) :
    return PN[0]

# Anak :  PohonN-ner tidak kosong --> list of PohonN-ner
# Anak(PN) adalah anak dari PN
def Anak(PN) :
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
#isTreeNEmpty : PohonN-ner ---> boolean
#isTreeNEmpty(PN) adalah predikat apakah pohon kosong
def isTreeNEmpty(PN) :
    return PN == []

#isOneElmt : PohonN-ner ---> boolean
#isOneElmt(PN) adalah predikat apakah pohon hanya memiliki satu elemen
def isOneElmt(PN) :
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(Anak(PN)) == True)


# DEFINISI DAN SPESIFIKASI FUNGSI LAIN

# NbElmt : PohonN-ner ---> integer>=0
# NbElmt (PN) adalah fungsi rekursif untuk menghitung jumlah elemen pada pohon
def NbElmt(PN) :
    if isTreeNEmpty(PN) :
        return 0
    elif isOneElmt(PN) :
        return 1
    else :
        return 1 + NbElmt(Anak(PN)[0]) + NbElmtChild(Anak(PN)[1:])


#NbElmtChild : PohonN-ner --> integer>= 0
#NbElmtChild (PN) adalah fungsi rekursif untuk menghitung child dari pada sebuah pohon. Fungsi ini adalah fungsi tambahan untuk NBElmt.
def NbElmtChild(PN) :
    if isTreeNEmpty(PN) :
        return 0
    else :
        return NbElmt(PN[0]) + NbElmtChild(PN[1:])

# NbDaun : PohonN-ner ---> integer>=0
# NbDaun(PN) aadalah fungsi rekursif untuk menghitung jumlah daun pada pohon
def NbDaun(PN) :
    if isTreeNEmpty(PN) :
        return 0
    elif isOneElmt(PN) and isTreeNEmpty(Anak(PN)) : #syarat daun
        return 1
    else :
        return NbDaunChild(Anak(PN))

# NbDaunChild : PohonN-ner ---> integer>= 0
# NbDaunChild(PN) adalah fungsi rekursif untuk menghitung jumlah daun dari sebuah pohon. Fungsi ini adalah fungsi tambahan untuk NBDaun.
def NbDaunChild(PN) :
    if isTreeNEmpty(PN) :
        return 0
    else :
        return NbDaun(PN[0]) + NbDaunChild(PN[1:])

def isMemberTree(E,PN) :
    if isTreeNEmpty(PN) :
        return False
    # elif IsEmpty(E) :
    #     return False
    # elif isOneElmt(PN) :
    #     return Akar(PN) == E
    else :
        if Akar(PN) == E :
            return True
        else :
            return isMemberTreeChld(E,Anak(PN))

def isMemberTreeChld(E,PN) :
    if isTreeNEmpty(PN) :
        return False
    # elif IsEmpty(E) :
    #     return False
    # elif isOneElmt(PN) :
    #     return Akar(PN) == E
    else :
        if Akar(PN) == E :
            return True
        else :
            # return isMemberTree(E,PN[1:]) 
            return isMemberTree(E, Akar(PN)) or isMemberTreeChld(E, Tail(PN))

# Test case
T2 = makePN('A', [
        makePN('B', [
            makePN('C', [
                'D',[]
                ])
            ]), 
        makePN('E', [
            makePN('F', [])
            ])
        ])

T2 = makePN('A', [
        makePN('B', [
            makePN('C', [
                makePN('D',[])
                ])
            ]), 
        makePN('E', [
            makePN('F', [])
            ])
        ])

# Test cases
print(isMemberTree('F', T2))  # Expected output: True
print(isMemberTree('H', T2))  # Expected output: False
print(isMemberTree([], T2))   # Expected output: False