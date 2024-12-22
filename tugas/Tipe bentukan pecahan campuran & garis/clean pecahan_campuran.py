# Nama File : pecahan_campuran.py
# Deskripsi : membuat tipe bentukan pecahan campuran beserta konstruktor dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 11 Oktober 2024


def bil (P) :
    return P[0]

def num (P) :
    return P[1]

def denum (P) :
    return P[2]

def MakePecahanc (b, n, d) :
    return [b, n, d]

def MakePecahan (n, d) :
    return [n, d]

def KonversiPecahan (P) :
    return MakePecahan(
            bil(P) * denum(P) + num(P), denum(P)
        )

def KonversiReal (P) :
    return numc(P) / denum(P)

def AddP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) // (denum(P1) * denum(P2)),
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) - ((denum(P1) * denum(P2)) * 
        (numc(P1) * denum(P2) + numc(P2) * denum(P1)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )
   
def SubP (P1, P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) // (denum(P1) * denum(P2)),
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) - ((denum(P1) * denum(P2)) * 
        (numc(P1) * denum(P2) - numc(P2) * denum(P1)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )
   
def DivP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * denum(P2)) // (denum(P1) * numc(P2)),
        (numc(P1) * denum(P2)) - (denum(P1) * numc(P2)) * 
        ((numc(P1) * denum(P2)) // (denum(P1) * numc(P2))),
        (denum(P1) * numc(P2))
    )
   
def MulP (P1,P2) :
    return MakePecahanc(
        (numc(P1) * numc(P2)) // (denum(P1) * denum(P2)),
        (numc(P1) * numc(P2)) - (denum(P1) * denum(P2)) * 
        ((numc(P1) * numc(P2)) // (denum(P1) * denum(P2))),
        denum(P1) * denum(P2)
    )

def numc (P) :
    return bil(P) * denum(P) + num(P)

def IsEqP (P1,P2) :
    return numc(P1) * denum(P2) == numc(P2) * denum(P1)
   
def IsLtP (P1,P2) :
    return numc(P1) * denum(P2) < numc(P2) * denum(P1)
   
def IsGtP (P1,P2) :
   return numc(P1) * denum(P2) > numc(P2) * denum(P1)


# APLIKASI

P1 = MakePecahanc(2, 1, 2)
P2 = MakePecahanc(1, 1, 2)
print(KonversiPecahan(P1))  # [5, 2]
print(KonversiPecahan(P2))  # [3, 2]
print(KonversiReal(P1))     # 2.5
print(KonversiReal(P2))     # 1.5
print(AddP(P1, P2))     # [4, 0, 4]
print(SubP(P1, P2))     # [1, 0, 4]
print(DivP(P1, P2))     # [1, 4, 6]
print(MulP(P1, P2))     # [3, 3, 4]
print(IsEqP(P1, P2))    # False
print(IsLtP(P1, P2))    # False
print(IsGtP(P1, P2))    # True