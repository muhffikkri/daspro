# NAMA: Muhammad Fikri 
# NIM : 24060124130069

def IsEmpty(L) :
    return L == []

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

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
            if IsPrima(FirstElmt(S)) : 
                return FirstElmt(S) + jumlahPrima(Tail(S))
            else : 
                return jumlahPrima(Tail(S))
        elif IsList(FirstElmt(S)) : 
            return jumlahPrima(FirstElmt(S)) + jumlahPrima(Tail(S))
        else : 
            return jumlahPrima(Tail(S))


        
import ast


list_of_list = ast.literal_eval(input())
print(jumlahPrima(list_of_list))