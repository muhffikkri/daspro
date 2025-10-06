"""
Sebagai mahasiswa Informatika sejati, Baygon ingin tahu mata kuliah apa yang sedang dijadwalkan pada hari tertentu di jam tertentu. Jadwal kuliah yang sudah ditentukan oleh departemen Baygon berkuliah adalah sebagai berikut:

Senin 	13-15 	→ Dasar Pemrograman
Selasa 	13-15 	→ Aljabar Linier
Rabu 	07-10 	→ Dasar Sistem
Rabu 	15-16 	→ Bahasa Inggris I
Kamis 	07-09 	→ Pancasila
Kamis 	13-15 	→ Matematika I
Jumat 	07-09 	→ Bahasa Indonesia
Jumat 	13-16 	→ Struktur Diskrit
Jika ada, keluarkan string Nama Matkul (sesuai dengan diatas), jika tidak ada maka keluarkan "Tidak ada". Apabila ada lebih dari satu dalam interval yang diberikan, pisahkan mata kuliah dengan &. Misal, "Bahasa Indonesia & Struktur Diskrit"

Input Format

SearchJadwal(hari, awal, akhir)
Constraints

hari	: "sen"|"sel"|"rab"|"kam"|"jum"|"sab"|"min"
awal	: integer
akhir	: integer
dimana , dan tidak ada kondisi multi-hari.

Output Format

[Mata Kuliah] | "Tidak ada"
Sample Input 0

SearchJadwal("sen", 12, 14)
Sample Output 0

Dasar Pemrograman
Explanation 0

Di interval 12-14, Baygon ada mata kuliah Dasar Pemrograman pada pukul 13-15.

Sample Input 1

SearchJadwal("jum", 8, 16)
Sample Output 1

Bahasa Indonesia & Struktur Diskrit
Explanation 1

Baygon memiliki jadwal Bahasa Indonesia dan Struktur Diskrit pada rentang jam 8 sampai 16.
"""


def SearchJadwal(hari:"str", awal:int, akhir:int)-> str:
    if not (0 <= awal <= 24 and 0 <= akhir <= 24):
        return "Tidak ada"
    
    if hari == "sen":
        if 13 < akhir and 15 > awal:
            return "Dasar Pemrograman"
        else:
            return "Tidak ada"
    elif hari == "sel":
        if 13 < akhir and 15 > awal:
            return "Aljabar Linier"
        else:
            return "Tidak ada"
    elif hari == "rab":
        if (7 < akhir and 10 > awal) and (15 < akhir and 16 > awal):
            return "Dasar Sistem & Bahasa Inggris I"
        elif 7 < akhir and 10 > awal:
            return "Dasar Sistem"
        elif 15 < akhir and 16 > awal:
            return "Bahasa Inggris I"
        else:
            return "Tidak ada"
    elif hari == "kam":
        if (7 < akhir and 9 > awal) and (13 < akhir and 15 > awal):
            return "Pancasila & Matematika I"
        elif 7 < akhir and 9 > awal:
            return "Pancasila"
        elif 13 < akhir and 15 > awal:
            return "Matematika I"
        else:
            return "Tidak ada"
    elif hari == "jum":
        if (7 < akhir and 9 > awal) and (13 < akhir and 16 > awal):
            return "Bahasa Indonesia & Struktur Diskrit"
        elif 7 < akhir and 9 > awal:
            return "Bahasa Indonesia"
        elif 13 < akhir and 16 > awal:
            return "Struktur Diskrit"
        else:
            return "Tidak ada"
    else:
        return "Tidak ada"

# JANGAN DIUBAH!
print(eval(input()))