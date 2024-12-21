# from list import *
# from list_of_list import *
# from binaryTree import *
def IsEmpty(L) :
    return L == []

def Akar(P):
    return P[0] 

def max2(a, b) :
    if a > b : 
        return a
    else : 
        return b
    
def min2(a, b) :
    if a < b : 
        return a
    else : 
        return b
    
def isMember(e, L) : 
    if IsEmpty(L) : 
        return False
    else : 
        if e == FirstElmt(L) : 
            return True
        else : 
            return isMember(e, Tail(L))
        
def Konso(e, L) : 
    return [e] + L

def Konsi(L, e) :
    return L + [e]

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

def Head(L) :
    return L[:-1]

def Right(P):
    return P[2] 

def Left(P):
    return P[1] 

def IsAtom(S): 
    return type(S) != list 

def IsList(S): 
    return type(S) == list

def IsTreeEmpty(T):
    return T == []

def IsOneElmt(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))

def MakePB(A, L, R):
    return [A, L, R]

def IsUnerLeft(T) :
    return (not IsTreeEmpty(Left(T))) and (IsTreeEmpty(Right(T)))

def IsBiner(T) :
    return (not IsTreeEmpty(Left(T))) and (not IsTreeEmpty(Right(T)))

def PrintBinaryTreeHelp(T, indent):
    if T != []:
        print(indent + str(Akar(T)))
        PrintBinaryTreeHelp(Left(T), indent + '\t')
        PrintBinaryTreeHelp(Right(T), indent + '\t')
    else:
        print(indent + "[]")

def PrintBinaryTree(T):
    PrintBinaryTreeHelp(T, '')


print("==" * 20)
print("SOAL UAS 2021")
# ======= SOAL UAS 2021 =======
# 1. 
#   a. max_list()
#   b. min_list()

# max_list: list -> integer
# Mencari nilai maksimum dalam sebuah list
def max_list(L) :
    if IsEmpty(L) : 
        return 0
    else : 
        return max2(FirstElmt(L), max_list(Tail(L)))

# min_list: list -> integer
# Mencari nilai minimum dalam sebuah list
def min_list(L) :
    if IsEmpty(L) : 
        return 0
    else : 
        return min2(FirstElmt(L), min_list(Tail(L)))

print("==" * 20)
print("SOAL 1")
L1 = [19, 21, 25, 11, 14, -13, 10 ,19, 10]
print(f"L1 = {L1}")
print(f"max_list ---> {max_list(L1)}")  # Output: 25
print(f"min_list ---> {min_list(L1)}")  # Output: 25



# 2.
#   a. total_elemen_daun()
#   b. max_elemen_daun()
#   c. total_elemen_node()
#   d. rata2_elemen_node()
#   e. BST()

# total_elemen_daun: tree -> integer
# Mencari total elemen daun dalam sebuah tree
def total_elemen_daun(T):
    if IsTreeEmpty(T):
        return 0
    if IsOneElmt(T) : 
        return Akar(T)
    else:
        return total_elemen_daun(Left(T)) + total_elemen_daun(Right(T))
            
# max_elemen_daun: tree -> integer
# Mencari nilai maksimum elemen daun dalam sebuah tree
def max_elemen_daun(T) :
    if IsTreeEmpty(T):
        return 0
    if IsOneElmt(T) : 
        return Akar(T)
    else:
        return max2(max_elemen_daun(Left(T)), max_elemen_daun(Right(T)))
    
# total_elemen_node: tree -> integer
# Mencari total elemen node dalam sebuah tree
def total_elemen_node(T) :
    if IsTreeEmpty(T):
        return 0
    else:
        return Akar(T) + total_elemen_node(Left(T)) + total_elemen_node(Right(T))

# Fungsi tambahan untuk rata2_elemen_node()
# nb_node: tree -> integer
def nb_node(T) : 
    if IsTreeEmpty(T):
        return 0
    else:
        return 1 + nb_node(Left(T)) + nb_node(Right(T))

# rata2_elemen_node: tree -> real
# Mencari rata-rata elemen node dalam sebuah tree
def rata2_elemen_node(T) : 
    if IsTreeEmpty(T):
        return 0
    else:
        return total_elemen_node(T) / nb_node(T)

# BST: tree -> integer
# Mencari apakah sebuah nilai di dalam binary tree
def BST(T, e) :
    if IsTreeEmpty(T) : 
            return False
    else : 
        # if IsOneElmt(T) : 
        #     if e == Akar(T):
        #         return True
        #     else :
        #         return False
        # else :
            if Akar(T) == e : 
                return True        
            else : 
                return BST(Left(T), e) or BST(Right(T), e)
                # if IsBiner(T) : 
                #     return BST(Left(T), e) or BST(Right(T), e)
                # else : 
                #     if IsUnerLeft(T) : 
                #         return BST(Left(T), e)
                #     else : 
                #         return BST(Right(T), e)


T = MakePB(50, 
            MakePB(17, 
                MakePB(12, 
                       MakePB(9, [], []), 
                       MakePB(14, [], [])
                       ),
                MakePB(23, 
                        [],
                       MakePB(19, [], [])
                      )
                ),  
            MakePB(72, 
                   MakePB(54, 
                          MakePB(67, [], []), 
                          []), 
                   MakePB(76, [], []), 
                   ) 
                )

print(BST(T, 17))

print("==" * 20)
print("SOAL 2")
print("tree : ")
PrintBinaryTree(T)
print("")
print(f"total_elemen_daun(T) ---> {total_elemen_daun(T)}")
print(f"max_elemen_daun(T) ---> {max_elemen_daun(T)}")
print(f"total_elemen_node(T) ---> {total_elemen_node(T)}")
print(f"rata2_elemen_node(T) ---> {rata2_elemen_node(T)}")
print("==" * 20)



# 3. 
#   a. kelipatan5()
#   b. bukan_kelipatan5()
# lambda => anonymous function atau fungsi tanpa nama yang fungsi nya sama seperti fungsi pada umum nya (mengembalikan nilai)
IsMultipleOF5 = lambda x : x % 5 == 0

# bukan_kelipatan5: list -> list
# mengembalikan list yang berisi elemen yang bukan kelipatan 5
def bukan_kelipatan5(L) : 
    if IsEmpty(L) : 
        return []
    else : 
        if IsMultipleOF5(FirstElmt(L)) : 
            return bukan_kelipatan5(Tail(L))
        else : 
            return Konso(Akar(L), bukan_kelipatan5(Tail(L)))

# kelipatan5: list -> list
# mengembalikan list yang berisi elemen yang kelipatan 5
def kelipatan5(L) :
    if IsEmpty(L) : 
        return []
    else : 
        if IsMultipleOF5(FirstElmt(L)) : 
            return Konso(Akar(L), kelipatan5(Tail(L)))
        else : 
            return kelipatan5(Tail(L))

print("SOAL 2")
L1 = [60, 18, 7, 20, 19, 23, 50]
L2 = kelipatan5(L1)
L3 = bukan_kelipatan5(L1)

print(f"L1 = {L1}")
print(f"L2 = {L2} ---> (Kelipatan 5)")
print(f"L3 = {L3} ---> (Bukan Kelipatan 5)")
print("==" * 20)


# Soal Pak Adi
print("Soal Pak Adi")
print("Mencari sebuah nilai maksimal ganjil yang berada di sebuah binary serach tree")
print("")

IsEven = lambda n : n % 2 == 0

# SearchMaxOdd: tree -> integer
# Mencari sebuah nilai maksimal ganjil yang ada di sebuah tree
def SearchMaxOdd(T) : 
    if IsEmpty(T) : 
        return 0
    else : 
        if IsEven(Akar(T)) :
            return max2(0, max2(SearchMaxOdd(Left(T)), SearchMaxOdd(Right(T))))
        else : 
            return max2(Akar(T), max2(SearchMaxOdd(Left(T)), SearchMaxOdd(Right(T))))
        
def SearchMaxEven(T) : 
    if IsEmpty(T) : 
        return 0
    else : 
        if not IsEven(Akar(T)) :
            return max2(0, max2(SearchMaxEven(Left(T)), SearchMaxEven(Right(T))))
        else : 
            return max2(Akar(T), max2(SearchMaxEven(Left(T)), SearchMaxEven(Right(T))))

print("tree : ")
PrintBinaryTree(T)
print("")
print(f"SearchMaxOdd(T) ---> {SearchMaxOdd(T)}")
print(f"SearchMaxEven(T) ---> {SearchMaxEven(T)}")
print("==" * 20)

# minus: list, list -> list 
# mengembalikan sebuah list dengan membuang sebuah elemen jika elemen tersebut ada di list lainnya
def minus(A, B) :
    if IsEmpty(A) : 
        return []
    else : 
        if isMember(FirstElmt(A), B) : 
            return minus(Tail(A), B)
        else : 
            return Konso(FirstElmt(A), minus(Tail(A), B))

A = [5, 12, 16, 7, 19, 25, 30]
B = [12, 7, 25]
print(f"A = {A}")
print(f"B = {B}")
print(f"minus(A, B) = {minus(A, B)}")

print("==" * 20)
print("SOAL UAS 2023")
# 1. FilterGenap()

# FilterGenap: list -> list
# Mengembalikan list dengan nilai nya berupa bilangan genap
def FilterGenap(L) :
    if IsEmpty(L) : 
        return []
    else : 
        if FirstElmt(L) % 2 == 0 : 
            return Konso(Akar(L), FilterGenap(Tail(L)))
        else : 
            return FilterGenap(Tail(L))

L1 = [6, 3, 1, 28, 12, 9, 4]
print(f"L1 = {L1}")
print(f"FilterGenap(L1) ---> {FilterGenap(L1)}")
print("==" * 20)

# 2. IsContainList

# IsContainList: ListOfList -> boolean
# mengembalikan nilai true jika list of list mengandung list
def IsContainList(LoL) : 
    if IsEmpty(LoL) : 
        return False
    else : 
        if IsAtom(FirstElmt(LoL)) : 
            return False or IsContainList(Tail(LoL))
        else : 
            return True or IsContainList(Tail(LoL))
        
LoL = [6, [3, 1], [28, 12, 9], 4]
print(f"LoL = {LoL}")
print(f"IsContainList(LoL) ---> {IsContainList(LoL)}")
print("==" * 20)

# no 4 Pohon N-Aire
# SubTX: x, PohonN-aire -> PohonN-aire
# Basis : IsEmpty()
# Rekurens : 
#       if Akar(T) = x : MakePN(Akar(T), Anak(T)) |Atau bisa juga ditulis return T aja| T
#       else : 
#           SubTX(x, Anak(T))

# no 5. Max elemen Binary Tree bisa dibagi 4 atau tidak 

# IsMaxBSTDivBy4: BST --> boolean
# Mengembalikan nilai true jika max elemen dalam sebuah BST bisa dibagi oleh 4 (habis dibagi 4)
def IsMaxBSTDivBy4(BST) : 
    return MaxBST(BST) % 4 == 0

# MaxBST: BST --> integer
# Mengembalikan nilai maksimal dari sebuah BST
def MaxBST(BST) : 
    if IsEmpty(BST) :
        return 0
    else :
        if IsBiner(BST) : 
            return max2(Akar(BST), max2(MaxBST(Left(BST)), MaxBST(Right(BST))))
        else : 
            # hanya cek ke kanan karna nilai max pasti ke kanan
            # kalau anak kanan kosong semua nilai max nya pasti akar
            return max2(Akar(BST), MaxBST(Right(BST)))
                
print("tree : ")
PrintBinaryTree(T)
print("")
print(f"Nilai Maksimum di tree : {MaxBST(T)}")
print(f"{MaxBST(T)} / 4 = {MaxBST(T)/4}")
print(f"IsMaxBSTDivBy4(T) ---> {IsMaxBSTDivBy4(T)}")


L = [12, 51, 123, 42]

def insert(x, L) :
    if IsEmpty(L) : 
        return Konso(x, L)
    else : 
        if x <= FirstElmt(L) : 
            return Konso(x, L)
        else : 
            return Konso(FirstElmt(L), insert(x, Tail(L)))

def insort(L) : 
    if IsEmpty(L) : 
        return []
    else : 
        return insert(FirstElmt(L), insort(Tail(L)))

print(L)
print(insort(L))



# def bukan_kelipatan5(L) : 
#     if IsEmpty(L) : 
#         return []
#     else : 
#         if IsMultipleOF5(FirstElmt(L)) : 
#             return bukan_kelipatan5(Tail(L))
#         else : 
#             return Konso(Akar(L), bukan_kelipatan5(Tail(L)))

# def kelipatan5(L) :
#     if IsEmpty(L) : 
#         return []
#     else : 
#         if IsMultipleOF5(FirstElmt(L)) : 
#             return Konso(Akar(L), kelipatan5(Tail(L)))
#         else : 
#             return kelipatan5(Tail(L))
        
k5 = lambda x : x % 5 == 0
bk5 = lambda x : x % 5 != 0
        
def Filter_List(fungsi, L) : 
    if IsEmpty(L) : 
        return []
    else : 
        if fungsi(FirstElmt(L)) : 
            return Konso(FirstElmt(L), Filter_List(Tail(L)))
        else : 
            return Filter_List(Tail(L))
    
# APLIKASI 
# ==> Filter_List(lambda x : x % 5 == 0, L)
# ==> Filter_List(lambda x : x % 5 != 0, L)


print("SOAL 2")
L1 = [60, 18, 7, 20, 19, 23, 50]
L2 = kelipatan5(L1)
L3 = bukan_kelipatan5(L1)



def anak(PN) : 
    return PN[1]

def contoh_fungsi_tree_n_aire(tree) : 
    if IsEmpty(tree) : 
        return # do something
    else : 
        return contoh_fungsi_tree_n_aire(anak(tree))
    

# no 4 Pohon N-Aire
# SubTX: x, PohonN-aire -> PohonN-aire
# Basis : IsEmpty()
# Rekurens : 
#       if Akar(T) = x : MakePN(Akar(T), Anak(T)) |Atau bisa juga ditulis return T aja| T
#       else : 
#           SubTX(x, Anak(T))


def main() : 
    print("SOAL 1")

if __name__ == "__main__" : 
    main()
    