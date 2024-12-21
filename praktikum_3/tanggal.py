# Nama File : tanggal.py
# Deskripsi : membuat tipe bentukan tanggal beserta konstruksi dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 24 September 2024

# DEFINISI TYPE
# type tanggal : <x:integer, y:integer, z:integer>
# {<x, y, z> adalah sebuah bentuk tanggal, dengan x adalah tanggal, y adalah bulan, dan z adalah tahun}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeTanggal: 2 integer --> array
# makeTanggal(x, y, z) membentuk sebuah array dari a dan b dengan a sebagai pembilang dan b sebagai penyebut}
# Realisasi fungsi makeTanggal
def makeTanggal (x, y, z) :
    return [x, y, z]
   
# tanggal: tanggal --> integer
# {tanggal (arr) mengembalikan komponen array ke-0 dari arr}
# Realisasi fungsi tanggal
def tanggal (arr) :
    return arr[0]

# tanggal: bulan --> integer
# {bulan (arr) mengembalikan komponen array ke-0 dari arr}
# Realisasi fungsi bulan
def bulan (arr) :
    return arr[1]

# tanggal: tahun --> integer
# {tahun (arr) mengembalikan komponen array ke-0 dari arr}
# Realisasi fungsi tahun
def tahun (arr) :
    return arr[2]
   
# pemb: 2 integer --> array
# {pemb (P) mengembalikan komponen array ke-1 dari P}
# Realisasi fungsi peny
def peny (P) :
    return P[1]
   

#APLIKASI
P = makeTanggal (1,2)
Q = makeTanggal (1,2)

