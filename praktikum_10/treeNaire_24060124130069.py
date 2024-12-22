# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) -> menghasilkan elemen pertama dari list L
# Realisasi
def FirstElmt(L) :
    return L[0]

# Tail : List tidak kosong -> List
# Tail(L) : menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L) :
    return L[1:]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A, PN) : 
    return [A, PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar : PohonN-ner tidak kosong -> elemen
# {Akar(PN) adalah akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A}
def akar(PN) : 
    return PN[0]

# Anak : PohonN-ner tidak kosong -> list of PohonN-ner
# {Anak(PN) adalah list of pohon N-ner yang merupakan anak anak (sub pohon) dari P. jika P adalah (A, PN) = anak (P) adalah PN}
def anak(PN) : 
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsTreeNEmpty : PohonN-ner -> boolean
# {IsTreeNEmpty(PN) true jika PN kosong : ()}
def isTreeNEmpty(PN) :
    return PN == []

# IsOneElmt : PohonN-ner -> boolean
# {IsOneElmt(PN) true jika PN hanya terdiri dari Akar}
def isOneElmt(PN) : 
    return (isTreeNEmpty(PN) == False) and isTreeNEmpty(anak(PN))

# NbElmt : PohonN-ner -> integer >= 0
# {NbElmt(PN) memberikan banyaknya node dari pohon P
# Basis 1 : NbElmt((A)\) = 1
# Rekurens : NbElmt ((A, PN)) = 1 + NbElmt(PN)}
def NbElmt(PN) : 
    # Basis : jika pohon kosong
    if isTreeNEmpty(PN) : 
        print("PN : ", PN)
        return 0
    
    # jika hanya ada satu elemen (akar saja)
    else :
        if isOneElmt(PN) : 
            print("PN : ", PN)
            return 1
            
        # Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
        # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap secara rekursif
        # Pertama pada anak pertama
        else : 
            print("PN : ", PN)
            return 1 + NbElmt(FirstElmt(anak(PN))) + NbElmtChild(Tail(anak(PN)))

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
# NbElmtChild : PohonN-ner -> integer
def NbElmtChild(PN) : 
    if isTreeNEmpty(PN) : 
        print("PN : ", PN)
        return 0
    else : 
        print("PN : ", PN)
        return NbElmt(FirstElmt(PN)) + NbElmtChild(Tail(PN))

# NbNDaun : PohonN-ner -> integer >= 0
# {NbNDaun(PN) memberikan banyaknya daun dari pohon P}
# Basis 1 : NbNDaun(A) = 1
# Rekurens : NbDaun((A, PN)) = NbNDaun(PN)
def NbNDaun(PN) : 
    if isTreeNEmpty(PN) : 
        print("PN : ", PN)
        return 0
    
    else :  
        if isOneElmt(PN) : 
            print("PN : ", PN)
            return 1
        else : 
            print("PN : ", PN)
            return NbNDaunChild(anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak 
# NbNDaunChild : PohonN-ner -> integer >= 0
def NbNDaunChild(PN) : 
    if isTreeNEmpty(PN) :
        print("PN : ", PN)
        return 0
    else :         
        print("PN : ", PN)
        return NbNDaun(FirstElmt(PN)) + NbNDaunChild(Tail(PN))

# searchXTree : elemen, PohonN-ner -> boolean
# {searchXTree(x, PN) mengecek apakah elemen x ada di dalam pohon}
def searchXTree(x, PN) : 
    if isTreeNEmpty(PN) : 
        return False
    
    else :
        if x == akar(PN) :
            return True
        else : 
            return searchXTreeChild(x, anak(PN))

# Fungsi tambahan untuk mengecek kecocokan x dengan anak anak dari pohon PN
# searchXTreeChild : elemen, PohonN-ner -> boolean
def searchXTreeChild(x, PN) : 
    if isTreeNEmpty(PN) :
        return False
    else : 
        return searchXTree(x, akar(PN)) or searchXTreeChild(x, Tail(PN))

T = makePN("A", 
        [
        makePN("B", 
            [
                makePN("Z", []), 
                makePN("Y", []), 
                makePN("X", []), 
                makePN("E", [])
            ]),
        makePN("F", 
            [
                makePN("G", []), 
                makePN("H", []), 
                makePN("I", []), 
                makePN("J", [])
            ]),
        makePN("C",
            [
                makePN("F", [])
            ])
        ]
    )

def isXIsSiblingofY(x, y, PN) : 
    if isTreeNEmpty(PN):
        return False
    else :
        if x == akar(PN) and y == akar(PN):
            return False
        elif x == akar(PN):
            return True
        else :
            return isXIsSiblingofY(x, y, anak(PN)) or isXIsSiblingofY(x, y, anak(PN))
        # return isXIsSiblingofY(x, y, Tail(PN))
# print(isXIsSiblingofY("B", "C", T)) # True

print(T)
print(NbElmt(T))
# print(NbNDaun(T))
# print(searchXTree("G", T))
# print(searchXTree("Z", T))
# print(searchXTree("F", T))

# def SubTX(x, PN) : 
#     if isTreeNEmpty(PN) : 
#         return []
#     else : 
#         if FirstElmt(PN) == x :
#             return makePN(FirstElmt(PN), anak(PN))
#         else :
#             return SubTXChild(x, anak(PN))

# def SubTXChild(x, PN) : 
#     if isTreeNEmpty(PN) :
#         return []
#     else : 
#         return SubTXChildChild(x, FirstElmt(PN), PN) 

# def SubTXChildChild(x, PN, child) :
#     if isTreeNEmpty(PN) :
#         return []
#     else : 
#         return SubTX(x, PN, child) + SubTXChildChild(x, anak(PN), child)
"""
T = makePN("A", 
        [
        makePN("B", 
            [
                makePN("Z", []), 
                makePN("Y", []), 
                makePN("X", []), 
                makePN("E", [])
            ]),
        makePN("F", 
            [
                makePN("G", []), 
                makePN("H", []), 
                makePN("I", []), 
                makePN("J", [])
            ]),
        makePN("C",
            [
                makePN("F", [])
            ])
        ]
    )
"""

def SubTX(x, PN) : 
    if isTreeNEmpty(PN) : 
        return []
    else : 
        if x == akar(PN) :
            return PN
        else :
            return SubTXChild(x, anak(PN))

def SubTXChild(x, PN) : 
    if isTreeNEmpty(PN) :
        return []
    else : 
        if not isTreeNEmpty(SubTX(x, FirstElmt(PN))):
            return SubTX(x, FirstElmt(PN))
        else:
            return SubTXChild(x, Tail(PN))
    
    
print(SubTX("Z", T))

def main() : 
    print("Tes")

if __name__ == "__main__" : 
    main()
    