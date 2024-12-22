from list import *

def IsEmpty(L) :
    return L == []

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

def Head(L) :
    return L[:-1]

def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

def operateVar(operator, S) : 
    if IsOneElmt(S) : 
        return FirstElmt(S)
    if operator == '+':
        return FirstElmt(S) + operateVar(operator, Tail(S))
    elif operator == '-':
        return FirstElmt(S) - operateVar(operator, Tail(S))
    elif operator == '*':
        return FirstElmt(S) * operateVar(operator, Tail(S))
    elif operator == '/':
        return FirstElmt(S) / operateVar(operator, Tail(S))


def EvaluateExpression(S) : 
    if IsEmpty(S) : 
        return []
    
    if FirstElmt(S) == "+" : 
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "-" : 
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "/" :
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "*" :
        return operateVar(FirstElmt(S), Tail(S))


#NAMA: Muhammad Fikri 
#NIM : 24060124130069

# DEFINISI DAN SPESIFIKASI# tail(L): List --> List
# tail(L) List dengan menghilangkan elemen pertamanya
def tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI
# firstElmt(L): List --> elemen
# firstElmt(L) Menampilkan elemen pertama dari List
def firstElmt(L):
    return L[0]

# DEFINISI DAN SPESIFIKASI
# isEmpty(L): List --> boolean
# isEmpty(L) mengecek apakah List kosong
def isEmpty(L):
    return L == []

def checkIfAllInt(L) : 
    if IsOneElmt(L) : 
        return type(firstElmt(L)) == int
    else : 
        return type(firstElmt(L)) == int and checkIfAllInt(tail(L))

def SumList(L):
    if isEmpty(L) : 
        return 0
    else : 
        if checkIfAllInt(L) : 
            return firstElmt(L) + SumList(tail(L))
        else : 
            return "males ah!"


# Fungsi untuk mengecek bilangan prima secara rekursif
def IsPrima(n, i=2):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    else:
        return IsPrima(n, i + 1)

def IsAtom(S): 
    return type(S) != list 

def IsList(S): 
    return type(S) == list

def jumlahPrima(S) : 
    if IsEmpty(S) : 
        return 0
    else : 
        if IsAtom(FirstElmt(S)) :
            print(FirstElmt(S), IsPrima(FirstElmt(S)))
            if IsPrima(FirstElmt(S)) : 
                return FirstElmt(S) + jumlahPrima(Tail(S))
            else : 
                return jumlahPrima(Tail(S))
        elif IsList(FirstElmt(S)) : 
            return jumlahPrima(FirstElmt(S)) + jumlahPrima(Tail(S))
        else : 
            return jumlahPrima(Tail(S))



print(jumlahPrima([1,[5,2,3],10,9,[7],[3,3]]))

# APLIKASI
# import ast


# list_of_list = ast.literal_eval(input())
# print(jumlahPrima(list_of_list))

def max2(a, b) :
    if a > b : 
        return a
    else : 
        return b

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
        if IsAtom(FirstElmt(S)) :
            return FirstElmt(S) * 1000000 + biaya(Tail(S))
        elif IsList(FirstElmt(S)) : 
            return biaya(FirstElmt(S))
        else : 
            return biaya(Tail(S))