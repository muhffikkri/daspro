# Nama File: determine.py
# Pembuat : JOVAN AMADEO HUTAGALUNG /24060125130077
# Tanggal: 19 September 2025
#Deskripsi: Menentukan apakah sebuah bilangan adalah bilangan prima atau bukan

#Definisi dan Spesifikasi
#Deetermine:int->str
#Determine(n) menentukan apakah n adalah bilangan prima atau bukan
#Realisasi
def Determine(n:int)->str:
    if n>0:
        if n%2==0:
            if n>2:
                return "Tidak"
            elif n==2:
                return "Ya"
        elif n%3==0:
            if n>3:
                return "Tidak"
            elif n==3:
                return "Ya"
        elif n%5==0:
            if n>5:
                return "Tidak"
            elif n==5:
                return "Ya"
        elif n%7==0:
            if n>7:
                return "Tidak"
            elif n==7:
                return "Ya"
        else:
            return "Ya"
#Aplikasi     
print(Determine(11))#Ya
print(Determine(15))#Tidak
print(Determine(2))#Ya
print(Determine(3))#Ya
print(Determine(4))#Tidak
print
#JANGAN DIUBAH!
print(eval(input()))