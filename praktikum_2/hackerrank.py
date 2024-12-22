# JAM PASIR AJAIB
def jam(j, m, s) : 
    if (    0 <= j 
        and j <= 24 
        and 0 <= m 
        and m < 60 
        and 0 <= s 
        and s < 60) : 
        return f"Jam: {j}, Menit: {m}, Detik: {s}"
    return "Waktu tidak valid" 

# LALU LINTAS LANGIT
def monitor_pesawat(x, y, z) : 
    if (x > 12000) : return "Terlalu Tinggi"
    elif (y > 900 or y < 200) : return "Kecepatan Berbahaya"
    elif (z < 20) : return "Bahan Bakar Rendah"
    elif (x < 5000 and (y > 200 and y < 900) and z > 50) : return "Aman untuk Mendarat"
    return "Berjalan Normal"

# JALAN SEMUT
def squareRoot(s) : return s**0.5
def square(s) : return s*s
def min2(i, j) : return i if(i < j) else j

def d1(x, y, z) : return squareRoot(((x + y) ** 2 + z ** 2))
def d2(x, y, z) : return squareRoot(((x + z) ** 2 + y ** 2))
def d3(x, y, z) : return squareRoot(((y + z) ** 2 + x ** 2))

def jalanSemut(x, y, z) :
    return round(min2(min2(d1(x, y, z),d2(x, y, z)), d3(x, y, z)), 3)

# BELAJAR TENANG
def BelajarTenang(dB, m):
    if 15 * (10 ** ((dB - 40) / 20)) <= m:
        return f"{15 * (10 ** ((dB - 40) / 20)):.3f} meter"
    return "Isi bensin dulu, bang"

# SEQUENCE BILANGAN PENYEBUT
def denumeratorSeq(x) :
    if((10**(len(x)) - 1)/int(x))%1 == 0: return f"Ada: {int((10**(len(x)) - 1)/int(x))}"
    return "Tidak ada"

# GRADIEN MAGIS
def square(s) : return s*s
def energi(x) : return (3*square(x)) + (2*x) - 5
def gradien(a,b) : return (energi(a) - energi(b)) / (a - b)

# SHOP SMART
def diskon(harga, persen):
    return harga - (harga * persen / 100)

def pajak(harga, persen):
    return harga + (harga * persen / 100)

def aturanDiskon(harga, kategori, VIP) : 
    if kategori == "elektronik":
        if VIP:
            return diskon(harga, 30)
        else:
            return diskon(harga, 10)
    if kategori == "pakaian":
        if VIP:
            return diskon(harga, 20)
        else:
            return diskon(harga, 5)
    if kategori == "makanan":
        if VIP:
            return diskon(harga, 15)
        else:
            return diskon(harga, 2)
    return harga
    
def aturanHari(harga, kategori, VIP, hari) : 
    if hari == "Jumat" or hari == "Sabtu":
        if VIP:
            return diskon(harga, 5)
    if hari == "Minggu":
        return pajak(harga, 5)
    if hari == "Rabu":
        if kategori == "pakaian":
            return diskon(harga, 5)
    return harga

def aturanLokasi(harga, lokasi) :
    if lokasi == "dalam negeri":
        return pajak(harga, 10)
    if lokasi == "luar negeri":
        return pajak(harga, 20)
    return harga

def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    return int(
        aturanLokasi(
            aturanHari(
                aturanDiskon(harga, kategori, VIP), 
                    kategori, VIP, hari), 
                lokasi)
    )

# PERPUSTAKAAN AGUNG
def TabelHari(Hari):
    if Hari == "senin":
        return (5000 + 6000 + 4000) / 3
    if Hari == "selasa":
        return (7000 + 5000 + 2000) / 3
    if Hari == "rabu":
        return (4500 + 3500 + 3000) / 3
    if Hari == "kamis":
        return (2900 + 2100 + 2000) / 3
    if Hari == "jumat":
        return (3000 + 3000 + 3000) / 3
    if Hari == "sabtu":
        return (2000 + 2500 + 2300) / 3
    if Hari == "minggu":
        return (1100 + 900 + 1000) / 3

def EstimateGreatLib(
    Hari,
    JamAwal,
    JamAkhir,
    Terbenam,
    Terbit,
    AhliStatistika,
    AhliMatematika,
    AhliIlmpuPerpustakaan,
    R,
):
    rataPengunjung = TabelHari(Hari)
    rangePengunjung = max(AhliStatistika, AhliMatematika, AhliIlmpuPerpustakaan) - min(
        AhliStatistika, AhliMatematika, AhliIlmpuPerpustakaan
    )

    if JamAwal >= Terbit and JamAkhir <= Terbenam:
        lamaWaktu = JamAkhir - JamAwal
        return round(lamaWaktu * rangePengunjung / rataPengunjung, 5)
    
    if JamAkhir <= Terbit or JamAwal >= Terbenam:
        lamaWaktu = JamAkhir - JamAwal
        return round((lamaWaktu * rangePengunjung / rataPengunjung) * (R / 100), 5)

    if JamAwal < Terbit and JamAkhir > Terbit and JamAkhir <= Terbenam:
        siang = JamAkhir - Terbit
        malam = Terbit - JamAwal
        return round(
            (
                (siang * rangePengunjung / rataPengunjung)
                + (malam * rangePengunjung / rataPengunjung) * (R / 100)
            )
            / 2,
            5,
        )
 
    if (
        JamAwal >= Terbit
        and JamAkhir > Terbenam
        and JamAkhir > JamAwal
        and JamAwal < Terbenam
    ):
        siang = Terbenam - JamAwal
        malam = JamAkhir - Terbenam
        return round(
            (
                (siang * rangePengunjung / rataPengunjung)
                + (malam * rangePengunjung / rataPengunjung) * (R / 100)
            )
            / 2,
            5,
        )
 
    if JamAwal < Terbit and JamAkhir > Terbenam:
        siang = Terbenam - Terbit
        malamSebelum = Terbit - JamAwal
        malamSesudah = JamAkhir - Terbenam
        return round(
            (
                (siang * rangePengunjung / rataPengunjung)
                + (malamSebelum * rangePengunjung / rataPengunjung) * (R / 100)
                + (malamSesudah * rangePengunjung / rataPengunjung) * (R / 100)
            )
            / 3,
            5,
        )
    