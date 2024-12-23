# Nama File : mahasiswa.py
# Deskripsi : membuat tipe bentukan MHS1, MHS2, dan MHS3 beserta konstruksi dan selektornya
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 24 September 2024

def make_MHS1(NIM, nama, tanggal_lahir) :
    return [NIM, nama, tanggal_lahir]

def select_NIM_MHS1(arr) :
    return arr[0]
    
def select_nama_MHS1(arr) :
    return arr[1]
    
def select_tanggal_lahir_MHS1(arr) :
    return arr[2]
    

def make_MHS2(NIM, kode_maktul, nilai) :
    return [NIM, kode_maktul, nilai]

def select_NIM_MHS2(arr) :
    return arr[0]
    
def select_kode_matkul_MHS2(arr) :
    return arr[1]
    
def select_nilai_MHS2(arr) :
    return arr[2]


def make_MHS3(kode_matkul, nama_matkul) : 
    return [kode_matkul, nama_matkul]

def select_kode_matkul_MHS3(arr) :
    return arr[0]
    
def select_nama_matkul_MHS3(arr) :
    return arr[1]

def hitungRangeNilai(arr) :
    return [
        select_kode_matkul_MHS2(arr),
        max(select_nilai_MHS2(arr)),
        min(select_nilai_MHS2(arr)),
        max(select_nilai_MHS2(arr)) - min(select_nilai_MHS2(arr))
    ]