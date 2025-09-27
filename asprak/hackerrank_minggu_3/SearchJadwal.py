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