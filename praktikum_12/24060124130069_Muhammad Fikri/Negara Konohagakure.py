# NAMA: Muhammad Fikri 
# NIM : 24060124130069

def max2(a, b) :
    if a > b : 
        return a
    else : 
        return b

def IsEmpty(L) :
    return L == []

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

def IsAtom(S): 
    return type(S) != list 

def IsList(S): 
    return type(S) == list

#Fungsi dan operator yang lain bisa ditambahkan sendiri
def MaxElmtList(S) :
    if IsEmpty(S) :
        return 0
    else : 
        if IsAtom(FirstElmt(S)) : 
            return max2(FirstElmt(S), MaxElmtList(Tail(S)))
        else : 
            return max2(MaxElmtList(FirstElmt(S)), MaxElmtList(Tail(S)))

def biaya(L) : 
    if IsEmpty(L) : 
        return 0
    else : 
        return MaxElmtList(FirstElmt(L)) * 1000000 + biaya(Tail(L))
#APLIKASI

import ast
list_of_list = ast.literal_eval(input())
print(biaya(list_of_list))