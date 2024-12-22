from list import *
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
        