def BawaPayung(T:float, P:float)->str:
    if (T <= 100 and T >= 0) and (P <= 100 and P >= 0):
        if P >= 50 or T > 35:
            return "Bawa"
        else:
            return "Tidak bawa"

#JANGAN DIUBAH!
print(eval(input()))