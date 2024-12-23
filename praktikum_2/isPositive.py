"""
Maxwell, seorang penyihir angka yang memiliki ketertarikan khusus terhadap bilangan positif, memutuskan untuk memintamu membuat sebuah mantra ajaib. Dia berkata, "Buatkan aku sebuah fungsi yang bisa memberitahuku apakah sebuah bilangan termasuk dalam favoritku atau tidak. Ingat, aku menyukai semua bilangan positif—dan ya, bahkan angka 0 sekalipun!" Dengan kecepatan seorang programmer ulung, kamu menciptakan fungsi is_positif(x), yang dengan mudah dapat mendeteksi apakah sebuah angka termasuk dalam daftar kesukaan Maxwell. Jika bilangan tersebut lebih besar dari atau sama dengan nol, maka Maxwell akan tersenyum lebar, karena itu adalah angka favoritnya!

Input Format
is_positif(x)

Constraints
-100 ≤ x ≤ 100

Output Format
True / False

Sample Input 0
is_positif(1)
Sample Output 0
True

Sample Input 1
is_positif(-1)
Sample Output 1
False
"""

def is_positif(x: float) -> bool : 
    """Return true if x is positive"""
    return x >= 0

if __name__ == "__main__" : 
    print(is_positif(5)) # Output : True
    print(is_positif(1)) # Output : True
    print(is_positif(-5)) # Output : False
    print(is_positif(7)) # Output : True
    print(is_positif(2)) # Output : True