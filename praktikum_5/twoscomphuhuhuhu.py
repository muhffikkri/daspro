def Konsi(y,x):
    return y + [x]

def FirstElmt(x):
    if x != []:    
        return x[0]

def Tail(x):
    if x != []:
        return x[1:]

def Head(x):
    if x != []:
        return x[:-1]

def IsEmpty(x):
    if x == []:
        return True
    else:
        return False
    
def LastElmt(x):
    if x != []:
        return x[-1]

def NbElmnt(x):
    if IsEmpty(x):
        return 0
    else:
        return 1 + NbElmnt(Tail(x))

def Konso(e,L) :
    return [e] + L


def ones(L) :
    if IsEmpty(L) :
        return []
    else :
        if LastElmt(L) == 1 :
            return Konsi(ones(Head(L)),0)
        else : #LastElmt(L) == 0:
            return Konsi(ones(Head(L)),1)

print(ones([0,0,0,1,1]))

def add1(L) :
    if LastElmt(L) == 1 :
        return Konsi(add1(Head(L)),0)
    else :
        return Konsi(Head(L),1)
print(add1(ones([0,0,0,1,1])))
print(add1(ones([0,1,1,0,0])))

def Max(L) :
    return L[-5:]

def twoscomp(L1,L2) :
    if IsEmpty(L1) and IsEmpty(L2) :
        return []
    elif IsEmpty(L2) :
        return L1
    elif IsEmpty(L1) :
        return L2
    elif Head(L1) + [] :      
                return Konsi(Head(L1),0)
    elif Head(add1(ones(L2))) + [] :
                return Konsi(Head(add1(ones(L2))),0)
    else :
        if LastElmt(L1) + LastElmt(add1(ones(L2))) == 2 :
            return Konsi(twoscomp(add1(Head(L1)),Head(add1(ones(L2)))),0)
        elif LastElmt(L1) + LastElmt(add1(ones(L2))) == 1 :
            return Konsi(twoscomp(Head(L1),Head(ones(L2))),1)
        else :
            return Konsi(twoscomp(Head(L1),Head(ones(L2))),0)

print(add1(ones([0, 0, 1, 1, 1])))
print(twoscomp([0, 0, 1, 1, 1], [0, 0, 1, 1, 0]))
print(twoscomp([0, 1, 1, 0, 1], [0, 0, 1, 1, 1]))

print(twoscomp([0,0,0,0,1], add1(ones([0,0,0,0,1]))))

print(add1(ones([0,0,0,0,1])))