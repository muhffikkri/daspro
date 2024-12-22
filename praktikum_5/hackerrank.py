from list import Konso, Konsi, FirstElmt, Tail, Head, LastElmt, IsEmpty

def Laprak(R, N) :
    if IsEmpty(R) : 
        return 0
    else :
        if FirstElmt(R) == 1 and FirstElmt(N) >= 90 : 
            return 1 + Laprak(Tail(R), Tail(N))
        else :
            return Laprak(Tail(R), Tail(N))
        

def inversBit(bit) :
    return int(not bit)
    # if bit == 0 : 
    #     return 1 
    # else : 
    #     return 0

def inversLBit(lbit) :
    if IsEmpty(lbit) :
        return []
    else :
        return Konso(inversBit(FirstElmt(lbit)), inversLBit(Tail(lbit)))

def complement(lbit) :
    return addLBit(inversLBit(lbit), [0, 0, 0, 0, 1])

def addBit(Cin, bit1, bit2) :
    return Cin ^ bit1 ^ bit2

def coutBit(Cin, bit1, bit2) : 
    return (bit1 and bit2) or (Cin and (bit1 ^ bit2))

def addLBit(lbit1, lbit2, Cin=0):
    if IsEmpty(lbit1) and IsEmpty(lbit2):
        return []

    else : 
        return Konsi(
            addLBit(Head(lbit1), Head(lbit2), coutBit(Cin, LastElmt(lbit1), LastElmt(lbit2))),
            addBit(Cin, LastElmt(lbit1), LastElmt(lbit2))
        )
    
def twoscomp(lbit1, lbit2) :
    return addLBit(lbit1, complement(lbit2))
