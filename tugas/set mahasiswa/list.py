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

def IsEmpty(L) :
    return L == []

def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

def NbElmt(L) :
    if IsEmpty(L) :
        return 0
    else : 
        return 1 + NbElmt(Tail(L))

def ElmtkeN(n, L) : 
    if IsEmpty(L) : 
        return []
    else :
        if n == 1 :
            return FirstElmt(L)
        else : 
            return ElmtkeN(n - 1, Tail(L)) 
    
def isMember(e, L) : 
    if IsEmpty(L) : 
        return False
    else : 
        if e == FirstElmt(L) : 
            return True
        else : 
            return isMember(e, Tail(L))

def Copy(L) :
    if IsEmpty(L) : 
        return L
    else : 
        return Konso(FirstElmt(L), Copy(Tail(L)))

def Inverse(L) :
    if IsEmpty(L) : 
        return L
    else : 
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

def Konkat(L1, L2) :
    if IsEmpty(L2) :
        return L1
    else :
        return Konkat(Konsi(L1, FirstElmt(L2)), Tail(L2))

def SumElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return FirstElmt(L) + SumElmt(Tail(L))

def AvgElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return SumElmt(L) / NbElmt(L)

def max2(a, b) :
    if a > b : 
        return a
    else : 
        return b

def MaxElmt(L) :
    if IsEmpty(L) :
        return 0
    else : 
        return max2(FirstElmt(L), MaxElmt(Tail(L)))

def countMax(e, L) :
    if IsEmpty(L) :
        return 0
    else : 
        if e == FirstElmt(L) :
            return 1 + countMax(e, Tail(L))
        else : 
            return countMax(e, Tail(L))

def MaxNB(L) :
    if IsEmpty(L) :
        return 0
    else :
        return [MaxElmt(L), countMax(MaxElmt(L), L)]

def AddList(L1, L2) : 
    if IsEmpty(L1) :
        return []
    else : 
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

def IsPalindrom(L) : 
    if IsEmpty(L) :
        return True
    else : 
        if FirstElmt(L) == FirstElmt(Inverse(L)) : 
            return IsPalindrom(Head(Tail(L)))

