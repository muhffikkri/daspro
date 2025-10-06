"""
Legenda mencatat adanya cerita tentang suatu cermin ajaib di pedalaman Astral Forest. Cermin itu didesain oleh Lord Travich, seorang insinyur yang terkenal akan kejeniusan dunia, ia diasingkan oleh dunia itu sendiri. Tak membiarkan hal itu menakutinya, ia menciptakan sebuah cermin ajaib yang ia namakan Divine Mirror, sebuah cermin yang mampu membawa siapapun yang berani melihatnya kemanapun.

Hari demi hari kamu telusuri Astral Forest untuk menemukan Divine Mirror. Suatu ketika, kamu berhasil menemukannya. Tetapi sebelum kamu bisa menghampiri cermin tersebut, kamu tiba-tiba saja diteleportasi ke tempat lain. Awalnya kamu kebingungan, sehingga kamu menelusuri Astral Forest kembali untuk mencari Divine Mirror lagi. Setiap kali kamu meraihnya, hal yang sama terjadi. Kamu kemudian mengenali polanya dan mencatatnya di buku sakumu:

1. TELEPORTASI KE POSISI REFLEKSI SAAT CERMIN ADA DI JANGKAUAN
2. SETELAH TELEPORTASI, POSISI AKAN DIUBAH ANTARA 0, 90, 180, 270, ATAU 360 DERAJAT BERLAWANAN JARUM JAM.
Input Format

DivineMirror(P, RF, RT)
Constraints

P: Point
RF: character
RT: integer
dimana  hanya bisa berupa karakter  atau , dan  dengan syarat  kelipatan .

Output Format

Point
Sample Input 0

DivineMirror(MakePoint(2.0, 2.0), 'Y', 90)
Sample Output 0

(-2.0, -2.0)
Sample Input 1

DivineMirror(MakePoint(4.0, 2.0), 'Y', 360)
Sample Output 1

(-4.0, 2.0)
"""

# Nama/NIM:
# Tanggal:

# Definisi Point
# type Point: <x: real, y: real>
#     {<x, y> adalah tipe bentukan point pada koordinat kartesian.}
type Point = tuple[float, float]

# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# MakePoint: 2 real -> point
#     {MakePoint(x, y) membentuk tipe data point dari input (x, y).}
# Realisasi:
def MakePoint(x: float, y: float) -> Point:
    return (x, y)

# -------------------------------------
# Definisi dan Spesifikasi Selektor
# getAbsis(p): Point -> real
#     {getAbsis(p) mengembalikan absis dari point (p).}
# getOrdinat(p): Point -> real
#     {getOrdinat(p) mengembalikan ordinat dari point (p).}
# Realisasi:
def getAbsis(p: Point) -> float:
    return p[0]
def getOrdinat(p: Point) -> float:
    return p[1]
  
def DivineMirror(P: Point, RF: str, RT: int) -> Point:
    if P == MakePoint(0.0, 0.0):
        return MakePoint(0.0, 0.0)
    elif RF == "X":
        if RT == 0:
            return MakePoint(getAbsis(P), getOrdinat(P) * -1)
        elif RT == 90:
            return MakePoint(getOrdinat(P), getAbsis(P))
        elif RT == 180:
            return MakePoint(getAbsis(P) * -1, getOrdinat(P))
        elif RT == 270:
            return MakePoint(getOrdinat(P) * -1, getAbsis(P) * -1)
        elif RT == 360:
            return MakePoint(getAbsis(P), getOrdinat(P) * -1)
    elif RF == "Y":
        if RT == 0:
            return MakePoint(getAbsis(P) * -1, getOrdinat(P))
        elif RT == 90:
            return MakePoint(getOrdinat(P) * -1, getAbsis(P) * -1)
        elif RT == 180:
            return MakePoint(getAbsis(P), getOrdinat(P) * -1)
        elif RT == 270:
            return MakePoint(getOrdinat(P), getAbsis(P))
        elif RT == 360:
            return MakePoint(getAbsis(P) * -1, getOrdinat(P))

# --
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# --
# JANGAN DIUBAH
print(eval(input()))