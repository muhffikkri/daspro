"""
Sistem penanggalan planet Xaverich memiliki struktur yang lebih kompleks setelah ditambahkan elemen tahun. Setiap tahun di Xaverich terdiri dari 13 bulan dengan 28 hari per bulan. Tahun-tahun di Xaverich dibagi menjadi dua jenis:

Tahun biasa: Tahun yang tidak habis dibagi 21.
Tahun khusus: Tahun yang habis dibagi 21.
Aturan tambahan yang berlaku untuk tahun adalah sebagai berikut:

Jika tahun adalah tahun khusus, maka setiap hari ke-7 di setiap bulan adalah "Hari Pengingat" tanpa memperhatikan bulan atau pola hari biasa.
Selain itu, aturan hari di setiap bulan masih berlaku seperti sebelumnya:

Bulan 1 - 4: Hari ganjil adalah "Hari Kerja", hari genap adalah "Hari Libur".
Bulan 5 - 8: Hari kelipatan 3 adalah "Hari Istirahat", selain itu adalah "Hari Produktif".
Bulan 9 - 13: Hari ganjil adalah "Hari Pengingat", hari genap adalah "Hari Biasa".
Buat program yang menerima sebuah tanggal pada planet Xaverich untuk mengklasifikasi hari apa!

Input Format

ClassifyXaverichDate(TX)
Constraints

TX: TanggalXaverich
dimana komponen dari  memiliki constraint:

.
Output Format

str
Sample Input 0

ClassifyXaverichDate(MakeTanggalXaverich(6, 7, 2025))
Sample Output 0

Hari Istirahat
Sample Input 1

ClassifyXaverichDate(MakeTanggalXaverich(7, 3, 2100))
Sample Output 1

Hari Pengingat
Sample Input 2

ClassifyXaverichDate(MakeTanggalXaverich(5, 5, 2025))
Sample Output 2

Hari Produktif
"""

# Nama/NIM:
# Tanggal:

# Definisi TanggalXaverich
# type TanggalXaverich: <hari: int, bulan: int, tahun: int>
# {}
type TanggalXaverich = tuple[int, int, int]

# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# MakeTanggalXaverich: 3 integer -> TanggalXaverich
# {}
# Realisasi:
def MakeTanggalXaverich(hari: int, bulan: int, tahun: int) -> TanggalXaverich:
    return (hari, bulan, tahun)

# -------------------------------------
# Definisi dan Spesifikasi Selektor
# hari(TX): TanggalXaverich -> int
#     {}
# bulan(TX): TanggalXaverich -> int
#     {}
# tahun(TX): TanggalXaverich -> int
#     {}
# Realisasi:
def hari(TX: TanggalXaverich) -> int:
    return TX[0]
def bulan(TX: TanggalXaverich) -> int:
    return TX[1]
def tahun(TX: TanggalXaverich) -> int:
    return TX[2]
    
def ClassifyXaverichDate(d):
    if tahun(d) % 21 == 0:
        # Tahun khusus: setiap hari ke-7 adalah "Hari Pengingat"
        if hari(d) == 7:
            return "Hari Pengingat"
    
    # Aturan berdasarkan bulan
    if bulan(d) >= 1 and bulan(d) <= 4:
        # Bulan 1-4: Hari ganjil = "Hari Kerja", hari genap = "Hari Libur"
        if hari(d) % 2 == 1:
            return "Hari Kerja"
        else:
            return "Hari Libur"
    elif bulan(d) >= 5 and bulan(d) <= 8:
        # Bulan 5-8: Hari kelipatan 3 = "Hari Istirahat", selain itu = "Hari Produktif"
        if hari(d) % 3 == 0:
            return "Hari Istirahat"
        else:
            return "Hari Produktif"
    elif bulan(d) >= 9 and bulan(d) <= 13:
        # Bulan 9-13: Hari ganjil = "Hari Pengingat", hari genap = "Hari Biasa"
        if hari(d) % 2 == 1:
            return "Hari Pengingat"
        else:
            return "Hari Biasa"

# --
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# --
# JANGAN DIUBAH
print(eval(input()))