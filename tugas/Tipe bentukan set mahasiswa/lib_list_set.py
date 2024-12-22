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

def Rember(x,L) :
    if IsEmpty(L) :
        return L
    else : 
        if FirstElmt(L) == x :
            return Tail(L)
        else :
            return Konso(FirstElmt(L), Rember(x, Tail(L)))

def MultiRember(x, L) : 
    if IsEmpty(L) :
        return L
    else : 
        if FirstElmt(L) == x :
            return MultiRember(x, Tail(L))
        else :
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

def MakeSet(L) : 
    if IsEmpty(L) : 
        return []
    else : 
        if isMember(FirstElmt(L), Tail(L)) : 
            return Konso(FirstElmt(L), MakeSet(MultiRember(FirstElmt(L), Tail(L))))
        else : 
            return Konso(FirstElmt(L), MakeSet(Tail(L)))

def KonsoSet(e, H) : 
    if IsEmpty(H) : 
        return []
    else :
        if isMember(e, H) : 
            return H
        else : 
            return Konso(e, H)
        
def IsSet(L) : 
    if IsEmpty(L) : 
        return True

    else : 
        if isMember(FirstElmt(L), Tail(L)) : 
            return False
        else : 
            return IsSet(Tail(L))

def IsSubset(H1, H2) : 
    if IsEmpty(H1) : 
        return True
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return IsSubset(Tail(H1), H2)
        else : 
            return False

def IsEqualSet(H1, H2) :
    if NbElmt(H1) != NbElmt(H2) : 
        return False
    else :
        return IsSubset(H1, H2) and IsSubset(H2, H1)

def IsIntersect(H1, H2) : 
    if IsEmpty(H1) or IsEmpty(H2) : 
        return False
    else : 
        if isMember(FirstElmt(H1), H2) :
            return True 
        else : 
            return IsIntersect(Tail(H1), H2)
    
def MakeIntersect(H1, H2) :
    if IsEmpty(H1) : 
        return []
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else : 
            return MakeIntersect(Tail(H1), H2)

def MakeUnion(H1, H2) : 
    if IsEmpty(H1) and IsEmpty(H2) : 
        return []
    elif not IsEmpty(H1) and IsEmpty(H2) : 
        return H1
    elif IsEmpty(H1) and not IsEmpty(H2) : 
        return H2
    else : 
        if isMember(FirstElmt(H1), H2) :
            return MakeUnion(Tail(H1), H2)
        else : 
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))

def NbIntersect(H1, H2) : 
    if IsEmpty(H1) : 
        return 0
    else : 
        if isMember(FirstElmt(H1), H2) : 
            return 1 + NbIntersect(Tail(H1), H2)
        else : 
            return NbIntersect(Tail(H1), H2)

def NbUnion(H1, H2) : 
    if not IsEmpty(H1) and IsEmpty(H2) : 
        return 0
    elif IsEmpty(H1) and not IsEmpty(H2) : 
        return 0
    else : 
        if isMember(FirstElmt(H1), H2) :
            return 1 + NbUnion(Tail(H1), H2)
        else : 
            return 2 + NbUnion(Tail(H1), H2)
        