"""
Fahri hendak pergi keluar kos dan harus menentukan apakah ia perlu membawa payung atau tidak. Ia mendapat informasi cuaca hari ini berupa suhu dan probabilitas hujan.

Aturannya: - Jika probabilitas hujan ≥ 50%, Fahri harus membawa payung. - Jika suhu > 35°C meskipun probabilitas hujan rendah, Fahri juga akan membawa payung untuk berteduh. - Jika tidak keduanya, Fahri tidak membawa payung.

Memang, Fahri memiliki kemampuan untuk berpikir rasional. Namun, ia meminta bantuanmu, seorang mahasiswa Informatika, untuk membuat program yang menentukan keputusan apa yang harus Fahri ambil. Are you up for the challenge?

Input Format

BawaPayung(suhu, prob)
Constraints

T	: real
P	: real
dengan  dan 

Output Format

"Bawa" | "Tidak bawa"
Sample Input 0

BawaPayung(27.5, 24.6)
Sample Output 0

Tidak bawa
Explanation 0

Fahri tidak membawa Payung karena probabilitas hujan hanyalah 24,6% dan suhu saat ini hanya 27,5o derajat Celcius.

Sample Input 1

BawaPayung(26.5, 86.5)
Sample Output 1

Bawa
Explanation 1

Fahri membawa Payung karena probabilitas hujan adalah 86,5%.
"""

def BawaPayung(T:float, P:float)->str:
    if (T <= 100 and T >= 0) and (P <= 100 and P >= 0):
        if P >= 50 or T > 35:
            return "Bawa"
        else:
            return "Tidak bawa"

#JANGAN DIUBAH!
print(eval(input()))