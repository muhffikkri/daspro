# NAMA: Muhammad Fikri 
# NIM : 24060124130069

# DEFINISI DAN SPESIFIKASI# tail(L): List --> List
# tail(L) List dengan menghilangkan elemen pertamanya
def Tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI
# firstElmt(L): List --> elemen
# firstElmt(L) Menampilkan elemen pertama dari List
def FirstElmt(L):
    return L[0]

# DEFINISI DAN SPESIFIKASI
# isEmpty(L): List --> boolean
# isEmpty(L) mengecek apakah List kosong
def IsEmpty(L):
    return L == []

def Head(L) :
    return L[:-1]

def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

def checkIfAllInt(L) : 
    if IsOneElmt(L) : 
        return type(FirstElmt(L)) == int
    else : 
        return type(FirstElmt(L)) == int and checkIfAllInt(Tail(L))

def SumList(L):
    if IsEmpty(L) : 
        return 0
    else : 
        if checkIfAllInt(L) : 
            return FirstElmt(L) + SumList(Tail(L))
        else : 
            return "males ah!"
    
# APLIKASI
print(SumList([int(x) if x.isdigit() else x for x in input().split()]))