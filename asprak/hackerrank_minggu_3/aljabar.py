"""
Aku bingung... tak ada arah.

Aku diminta untuk membuat program fungsional untuk menghitung hasil pembagian antar akar-akar persamaan kuadrat  dengan masukan berupa 3 buah koefisien, yaitu a, b dan c.

Akar-akar yang sudah ditemukan harus dimutlakkan, lalu dibagi yang paling kecil dengan paling besar, sehingga rentang nilai keluaran selalu .

Jika digit belakang terlalu panjang, maka dibulatkan ke 5 digit belakang saja. Jika persamaan kuadrat bersifat imajiner, maka aku harus mengeluarkan -999.

Bisakah kamu membantuku...? :(

--

CATATAN:

Rumus pencari akar persamaan kuadrat:

Gunakan round(angka, x) untuk membulatkan, dimana angka diisi angka atau ekspresi tertentu, dan x diisi pembulatan sampai berapa digit.

Gunakan fungsi antara untuk mempermudah!

Gunakan Paradigma Fungsional. Artinya, tidak boleh ada memorisasi variabel.

Input Format

Aljabar(a, b, c)
Constraints

a, b, c: integer
Persamaan yang terbentuk dari koefisien a, b, dan c selalu persamaan kuadratik.

Output Format

real
dimana  jika persamaan riil dan  jika persamaan imajiner.

Sample Input 0

Aljabar(2, 4, 5)
Sample Output 0

-999
Explanation 0

Akar yang terbentuk dari persamaan  adalah imajiner. Maka, yang dikeluarkan adalah .image

Sample Input 1

Aljabar(1, -5, 6)
Sample Output 1

0.66667
Explanation 1

Akar dari persamaan  adalah  dan . Jika dimutlakkan,  adalah yang paling besar, maka hasil baginya adalah , yaitu 0.6666666 dst. Karena tidak berujung, maka dibulatkan ke 5 digit terakhir.
"""

def fxabs(x:int)->int:
    return (x if x >=0 else -x)
def akar1(a:int,b:int,c:int)->float:
    return (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
def akar2(a:int,b:int,c:int)->float:
    return (-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

def Aljabar(a:int,b:int,c:int)->float:
    if (b ** 2 - (4 * a * c)) >= 0:
        if fxabs(akar1(a,b,c)) <= fxabs(akar2(a,b,c)):
            return round(fxabs(akar1(a,b,c) / akar2(a,b,c)),5)
        elif fxabs(akar1(a,b,c)) > fxabs(akar2(a,b,c)):
            return round(fxabs(akar2(a,b,c) / akar1(a,b,c)),5)
    else:
        return -999

#JANGAN DIUBAH!
print(eval(input()))