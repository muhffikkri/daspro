from mahasiswa import *

def avgNilai(nilai):
    if IsEmpty(nilai):
        return 0
    else:
        return SumElmt(nilai) / NbElmt(nilai)

def lulus(mhs):
    if IsEmpty(mhs):
        return []
    else:
        if avgNilai(LastElmt(mhs)) >= 70:
            return Konso(LastElmt(mhs), lulus(Head(mhs)))
        else:
            return lulus(Head(mhs))

def tidakMengerjakanKuis(mhs, kelas):
    if IsEmpty(mhs):
        return []
    else:
        if FirstElmt(LastElmt(mhs)) == kelas and IsEmpty(LastElmt(FirstElmt(mhs))):
            return Konso(FirstElmt(mhs), tidakMengerjakanKuis(Head(mhs), kelas))
        else:
            return tidakMengerjakanKuis(Head(mhs), kelas)

def nilaiTertinggi(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return max2(MaxElmt(LastElmt(mhs)), nilaiTertinggi(Head(mhs)))

def mahasiswaTertinggiKelas(mhs, kelas):
    if IsEmpty(mhs):
        return []
    else:
        if FirstElmt(LastElmt(mhs)) == kelas:
            if MaxElmt(LastElmt(mhs)) == avgNilai(LastElmt(mhs)):
                return Konso(FirstElmt(mhs), mahasiswaTertinggiKelas(Head(mhs), kelas))
            else:
                return mahasiswaTertinggiKelas(Head(mhs), kelas)
        else:
            return mahasiswaTertinggiKelas(Head(mhs), kelas)

def jumlahTidakMengerjakanKuis(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return (1 if IsEmpty(LastElmt(FirstElmt(mhs))) else 0) + jumlahTidakMengerjakanKuis(Head(mhs))

def jumlahLulus(mhs):
    if IsEmpty(mhs):
        return 0
    else:
        return (1 if avgNilai(LastElmt(mhs)) >= 70 else 0) + jumlahLulus(Head(mhs))

def AddMahasiswa(mhsSet, mahasiswaBaru):
    if IsEmpty(mhsSet):
        return Konso(mahasiswaBaru, mhsSet) 
    else :
        if FirstElmt(mahasiswaBaru) == FirstElmt(FirstElmt(mhsSet)):
            return mhsSet  
        else : 
            return Konso(FirstElmt(mhsSet), AddMahasiswa(Tail(mhsSet), mahasiswaBaru)) 


# # Contoh penggunaan
# mhs = [
#     ["123", "Alice", "A", [80, 70, 75]],
#     ["124", "Bob", "A", [60, 50, 55]],
#     ["125", "Charlie", "B", [90, 85, 88]],
#     ["126", "David", "A", []],  # tidak mengerjakan kuis
# ]

# # Menggunakan fungsi-fungsi
# print("Mahasiswa yang lulus:", lulus(mhs))
# print("Mahasiswa yang tidak mengerjakan kuis di kelas A:", tidakMengerjakanKuis(mhs, "A"))
# print("Nilai tertinggi dari semua kelas:", nilaiTertinggi(mhs))
# print("Mahasiswa dengan nilai tertinggi di kelas A:", mahasiswaTertinggiKelas(mhs, "A"))
# print("Jumlah mahasiswa yang tidak mengerjakan kuis:", jumlahTidakMengerjakanKuis(mhs))
# print("Jumlah mahasiswa yang lulus:", jumlahLulus(mhs))

mhsSet = []  # Inisialisasi set mahasiswa

# Membuat mahasiswa baru
mahasiswa1 = ["123", "Ali", "A", [80, 70, 75]]
mahasiswa2 = ["124", "Bob", "A", [60, 50, 55]]
mahasiswa3 = ["125", "Cha", "B", [90, 85, 88]]
mahasiswa4 = ["123", "Dav", "A", [70, 80, 75]]

mhsSet = AddMahasiswa(mhsSet, mahasiswa1)
mhsSet = AddMahasiswa(mhsSet, mahasiswa2)
mhsSet = AddMahasiswa(mhsSet, mahasiswa3)
mhsSet = AddMahasiswa(mhsSet, mahasiswa4)  # Ini tidak akan menambah mahasiswa karena NIM sama

# Menampilkan set mahasiswa
print("Set Mahasiswa:")
print(mhsSet)