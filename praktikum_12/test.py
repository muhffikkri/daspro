# from LOL import *
# from list import *


# type shelf: <tag: string,
#               book: list of string>

# koleksi objek
# type shelves: <rakbuku: list of shelf>

# NOTE: tag dan book adalah komponen dari shelf
#       shelf adalah elemen dari shelves 

# --------------- LIBRARY LoL AND List ------------------

def MakeList(a):
    return [a]

def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def concatList(L1, L2):
    return L1 + L2

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

def FirstList(LoL):
    return LoL[0]

def LastList(LoL):
    return LoL[-1]

def HeadList(LoL):
    return LoL[:-1]

def TailList(LoL):
    return LoL[1:]

def IsEmpty(LoL):
    if LoL == []:
        return True
    else:
        return False

def IsAtom(LoL):
    if type(LoL) == list:
             return False
    else:
        return True

def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False


# --------------- FUNCTION USED IN ADDBOOKS --------------

# SELEKTOR
def getTag(shelf):
    return FirstElmt(shelf)

def getBooks(shelf):
    return LastElmt(shelf)

# FUNGSI KHUSUS
# bersifat opsional, tidak harus digunakan
# boleh buat fungsi antara sendiri

# makeShelf: string, list -> shelf
# fungsi ini membuat sebuah shelf baru dengan komponen tag dan book
def makeShelf(tag, book):
    return [tag, book]

# AddToShelf: string, list -> shelf
# fungsi ini menambahkan buku ke sebuah shelf dengan tag tertentu
def AddToShelf(tag, book):
    return [tag] + [book]

# ----------------- FUNCTION ------------------------

# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu
# def AddBooks(shelves, tag, book):
#     return

def insertBook(shelves, book) : 
    return Konso(getTag(shelves), MakeList(concatList(getBooks(shelves), book)))


def AddBooks(shelves, tag, book) : 
    if IsEmpty(shelves) : 
        return []

    if IsOneElmt(shelves) : 
        if getTag(FirstElmt(shelves)) == tag : 
            return MakeList(Konso(getTag(FirstElmt(shelves)), MakeList(concatList(FirstElmt((Tail(FirstElmt(shelves)))), book))))
        else : 
            if IsEmpty(book) : 
                return Konso(FirstElmt(shelves), [])
            else : 
                return Konso(FirstElmt(shelves), MakeList(makeShelf(tag, book)))
    
    else : 
        if getTag(FirstElmt(shelves)) == tag : 
            return Konso(insertBook(FirstElmt(shelves), book), Tail(shelves))

        else : 
            return Konso(FirstElmt(shelves), AddBooks(Tail(shelves), tag, book))

# ----------------- APLIKASI ------------------------

# AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers'])
# t = AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers'])
t = AddBooks([
            ['Novel', ['Toko Kelontong Namiya', 'Bumi', 'The Little Prince']], 
            ['Komputer', ['Clean Code', 'Modern OS', 'Computer Network', 'DSA', 'Algorithms']], 
            ['Biologi', ['Sobotta', 'The Selfish Gene', 'Kepunahan Keenam']], 
            ['Fisika', ['A Brief History of Time', 'The Elegant Universe', 'Astrofisika untuk Orang Sibuk']]
            ], "tes", [])
# t = AddBooks([['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']]], "Fisika", ['A Brief History of Time'])
# print(Tail(FirstElmt(t)))
print(IsEmpty(getBooks(FirstElmt(t))))
print(concatList(FirstElmt((Tail(FirstElmt(t)))), ["tes"]))

print(t)
# print(eval(input()))

# SEMANGAT ^^