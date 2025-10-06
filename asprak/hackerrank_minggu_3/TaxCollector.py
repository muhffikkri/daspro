"""
Rohsani adalah seorang pekerja biasa yang hari ini dilantik menjadi Direktur Keuangan di perkantorannya sebagai pemenang utama dalam giveaway yang diadakan di suatu instansi. Saat dia sedang menikmati jabatan barunya, ia tiba-tiba tersadar ada dokumen kantor di atas mejanya. Ia membuka dokumen tersebut dan melihat bahwa dokumen tersebut adalah rincian gaji karyawan.

"Karyawan digaji perjam ya bruv."
Lalu, ia tiba-tiba terpikir akan suatu hal. Merasa gajinya kurang untuk menghidupi biaya hidupnya yang baru, ia menerapkan kebijakan baru untuk setiap karyawan perusahaan.

Ia menetapkan bahwa sebelum hasil kumulatif gaji berdasarkan jam kerja karyawan dibagikan, gaji tersebut akan dipajak terlebih dahulu sesuai bayaran perjam karyawan dengan kriteria sebagai berikut:

 Pajak 15%
 Pajak 10%
 Pajak 5%
 Pajak 0%
Karena terlalu malas, Rohsani meminta bantuanmu untuk membuatkan program untuk melakukan komputasi tersebut. Bantulah Rohsani!

Input Format

TaxCollector(G, J)
Constraints

G	: real
J	: integer
dengan  dan 

Output Format

real
Sample Input 0

TaxCollector(55.0, 8)
Sample Output 0

396.0
Explanation 0

Karyawan tersebut bekerja selama 8 jam dengan gaji sebesar 55k/jam. Maka, ia kena pajak sebesar 10% dari gaji akhirnya.



"""

def TaxCollector(G:float,J:int)->float:
    if G >= 0 and J >= 0:
        if G < 50:
            return (G * J) * 0.85
        elif G <= 150 and G >= 50:
            return (G * J) * 0.9
        elif G <= 500 and G > 150:
            return (G * J) * 0.95
        else:
            return G * J

#JANGAN DIUBAH!
print(eval(input()))