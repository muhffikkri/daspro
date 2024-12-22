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
        return 0
    
    # jika hanya ada satu elemen (akar saja)
    else :
        if isOneElmt(PN) : 
            return 1
            
        # Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
        # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap secara rekursif
        # Pertama pada anak pertama
        else : 
            return 1 + NbElmt(FirstElmt(anak(PN))) + NbElmtChild(Tail(anak(PN)))

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
# NbElmtChild : PohonN-ner -> integer
def NbElmtChild(PN) : 
    if isTreeNEmpty(PN) : 
        return 0
    else : 
        return NbElmt(FirstElmt(PN)) + NbElmtChild(Tail(PN))

# NbNDaun : PohonN-ner -> integer >= 0
# {NbNDaun(PN) memberikan banyaknya daun dari pohon P}
# Basis 1 : NbNDaun(A) = 1
# Rekurens : NbDaun((A, PN)) = NbNDaun(PN)
def NbNDaun(PN) : 
    if isTreeNEmpty(PN) : 
        return 0
    
    else :  
        if isOneElmt(PN) : 
            return 1
        else : 
            return NbNDaunChild(anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak 
# NbNDaunChild : PohonN-ner -> integer >= 0
def NbNDaunChild(PN) : 
    if isTreeNEmpty(PN) :
        return 0
    else :         
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

# Fungsi untuk mengecek apakah x adalah sibling dari y
# Sibling adalah node yang memiliki parent yang sama
# isXSiblingY : elemen, elemen, PohonN-ner -> boolean
# Contoh : 
# S = makePN("A", [
#         makePN("B", 
#                 [
#                     makePN("D", [
#                         makePN("J", [])
#                     ]),
#                     makePN("E", [
#                         makePN("I", [])
#                     ])
#                 ]
#                ),
#         makePN("C", [
#                     makePN("F", []),
#                     makePN("G", [
#                         makePN("H", [])
#                     ])
#         ])
# ])
# [F, G] sibling
# [D, E] sibling
# [J, I] bukan sibling
# [I, H] bukan sibling
# isXSiblingY("F", "G", S) -> true
# isXSiblingY("D", "E", S) -> true
# isXSiblingY("J", "I", S) -> false
# isXSiblingY("I", "H", S) -> false
# def isXSiblingY(x, y, PN, parent = None) :
#     if isTreeNEmpty(PN) : 
#         return False
    
#     else :
#         return isXSiblingYChild(x, y, anak(PN), Tail(PN))

# # Fungsi tambahan untuk mengecek kecocokan x dan y di level berikutnya
# # ixXSiblingY : elemen, elemen, PohonN-ner -> boolean
# def isXSiblingYChild(x, y, PN, parent = None) : 
#     if isTreeNEmpty(PN) :
#         return False
#     else : 
#         return isXSiblingY(x, y, akar(PN), parent) or isXSiblingYChild(x, y, Tail(PN), parent)

# def isXSiblingY(x, y, PN):
#     if isTreeNEmpty(PN):
#         return False
    
#     children = anak(PN)
    
#     # Check if x and y are in the same list of children
#     if (akar(FirstElmt(children)) == x and searchXTree(y, children)) or (akar(FirstElmt(children)) == y and searchXTree(x, children)):
#         return True
    
#     # Recursively check in the children
#     return isXSiblingY(x, y, FirstElmt(children)) or isXSiblingY(x, y, Tail(children))

# # Helper function to get the first element of a list
# def FirstElmt(PN):
#     return PN[0] if PN else None

# ['A', 
#     [
#         ['B', 
#             [
#                 ['D', []], 
#                 ['E', []]
#             ]
#         ], 
#         ['C', 
#             [
#                 ['F', [
#                     ['G', []]
#                     ]
#                 ]
#             ]
#         ]
#     ]
# ]

T = makePN("A", 
        [
        makePN("B", 
            [
                makePN("D", []), 
                makePN("E", [])
            ]),
        makePN("C",
            [
                makePN("F", 
                    [
                        makePN("G", []),
                    ])
            ])
        ]
    )

print(T)
# print(isXSiblingY("F", "G", T)) # False
# print(isXSiblingY("F", "E", T)) # False
# print(isXSiblingY("D", "E", T)) # True
print(NbElmt(T))
print(NbNDaun(T))
print(searchXTree("G", T))
print(searchXTree("Z", T))
print(searchXTree("F", T))
print(FirstElmt(anak(T)))