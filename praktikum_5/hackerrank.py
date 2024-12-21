from list import Konso, Konsi, FirstElmt, Tail, Head, LastElmt, IsEmpty
from list import *

def Laprak(R: int, N: int) -> int :
    if IsEmpty(R) : 
        return 0
    else :
        if FirstElmt(R) == 1 and FirstElmt(N) >= 90 : 
            return 1 + Laprak(Tail(R), Tail(N))
        else :
            return Laprak(Tail(R), Tail(N))
        

def inversBit(bit: int) -> int :
    return int(not bit)

def inversLBit(lbit: list) -> list :
    if IsEmpty(lbit) :
        return []
    else :
        return Konso(inversBit(FirstElmt(lbit)), inversLBit(Tail(lbit)))

def complement(lbit: list) -> list :
    return addLBit(inversLBit(lbit), [0, 0, 0, 0, 1])

def addBit(Cin: int, bit1: int, bit2: int) -> int :
    # return Cin ^ bit1 ^ bit2
    return (Cin + bit1 + bit2) % 2

def coutBit(Cin: int, bit1: int, bit2: int) -> int : 
    # return (bit1 and bit2) or (Cin and (bit1 ^ bit2))
    return (Cin + bit1 + bit2) // 2

def addLBit(lbit1: list, lbit2: list, Cin: int=0) -> list : 
    if IsEmpty(lbit1) and IsEmpty(lbit2):
        return []

    else : 
        return Konsi(
            addLBit(Head(lbit1), Head(lbit2), coutBit(Cin, LastElmt(lbit1), LastElmt(lbit2))),
            addBit(Cin, LastElmt(lbit1), LastElmt(lbit2))
        )
    
def twoscomp(lbit1: list, lbit2: list) -> list :
    return addLBit(lbit1, complement(lbit2))

print(twoscomp([0, 0, 1, 1, 1], [0, 0, 1, 1, 0]))

# print("Hasil twoscomp([0, 0, 1, 1, 1], [0, 0, 1, 1, 0]):", twoscomp([0, 0, 1, 1, 1], [0, 0, 1, 1, 0]))
# print("Hasil twoscomp([0, 1, 1, 0, 1], [0, 0, 1, 1, 1]):", twoscomp([0, 1, 1, 0, 1], [0, 0, 1, 1, 1]))
# print("Hasil twoscomp([0, 0, 0, 0, 1], [0, 0, 0, 0, 1]):", twoscomp([0, 0, 0, 0, 1], [0, 0, 0, 0, 1]))
# print("Hasil twoscomp([1, 0, 0, 0, 0], [0, 0, 0, 0, 1]):", twoscomp([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))