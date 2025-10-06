"""
Kris dan Noelle akan melakukan perjalanan antariksa dari planet A menuju planet B menggunakan pesawat antariksa yang dilengkapi fitur-fitur canggih. Namun di hari mereka akan melakukan perjalanan tersebut, tiba-tiba saja matahari galaksi mereka mengeluarkan ledakan sinar-gamma dalam jumlah yang tak terduga. Hal ini membuat teknologi canggih yang akan mengcompute jarak perjalanan mereka ke planet B tidak stabil, sehingga tidak memungkinkan untuk menggunakan teknologi tersebut karena unreliable.

Setelah berjam-jam mencari solusi alternatif, Noelle menemukan sebuah artefak misterius di basementnya: SEBUAH KOMPUTER LAWAS! Komputer ini masih menggunakan bit 0 dan 1 untuk melakukan komputasi, sehingga meski inefisien, tapi resistan terhadap gangguan sinar-gamma. Sayangnya, Noelle maupun Kris tidak bisa memrogram dalam bahasa lawas tersebut.

Beruntungnya, mereka memiliki teman yang baik, yaitu ANDA, seorang sejarawan komputer. Bisakah kamu membantu mereka?

--

Notes:

Gunakan float(operand, 5) untuk membulatkan ke 5 digit belakang.

Input Format

DBT(tdp1, tdp2)
Constraints

tdp1, tdp2: Point
Jarak antara Titik tdp1 dan tdp2 pasti ada.

Output Format

float
Sample Input 0

DBT(Make3DPoint(0.0, 2.0, 5.0), Make3DPoint(7.0, 2.0, 3.0))
Sample Output 0

7.28011
Sample Input 1

DBT(Make3DPoint(1.5, -2.5, 3.5), Make3DPoint(-4.5, 5.5, -6.5))
Sample Output 1

14.14214
"""

# Nama/NIM:
# Tanggal:

# Definisi Point
# type Point: <x: real, y: real, z:real>
#     {<x, y, z> adalah tipe bentukan point tiga dimensi.}
type ThreeDPoint = tuple[float, float, float]

# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# Make3DPoint: 3 real -> point
#     {Make3DPoint(x, y, z) membentuk tipe data point 3D dari input (x, y, z).}
# Realisasi:
def Make3DPoint(x: float, y: float, z: float) -> ThreeDPoint:
    return (x, y, z)

# -------------------------------------
# Definisi dan Spesifikasi Selektor
# getAbsis(p): Point -> real
#     {getAbsis(p) mengembalikan absis dari point (p).}
# getOrdinat(p): Point -> real
#     {getOrdinat(p) mengembalikan ordinat dari point (p).}
# getApotema(p): Point -> real
#     {getApotema(p) mengembalikan apotema dari point (p).}
# Realisasi:
def getAbsis(p: ThreeDPoint) -> float:
    return p[0]
def getOrdinat(p: ThreeDPoint) -> float:
    return p[1]
def getApotema(p: ThreeDPoint) -> float:
    return p[2]

# -------------------------------------
# Definisi dan Spesifikasi Fungsi DBT
# DBT: ThreeDPoint, ThreeDPoint -> float
#     {DBT(tdp1, tdp2) menghitung jarak Euclidean antara dua titik 3D.}
# Realisasi:
def DBT(tdp1: ThreeDPoint, tdp2: ThreeDPoint) -> float:
    return round(
            (
                (
                    (getAbsis(tdp2) - getAbsis(tdp1)) * (getAbsis(tdp2) - getAbsis(tdp1)) + 
                    (getOrdinat(tdp2) - getOrdinat(tdp1)) * (getOrdinat(tdp2) - getOrdinat(tdp1)) + 
                    (getApotema(tdp2) - getApotema(tdp1)) * (getApotema(tdp2) - getApotema(tdp1))
                ) ** 0.5)
                ,5)

# JANGAN DIUBAH
print(eval(input()))

