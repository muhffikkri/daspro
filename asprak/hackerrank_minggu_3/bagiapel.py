"""
Kokoro adalah elf berambut putih yang baik hati. Di suatu hari, dia mendapatkan n buah apel untuk dibagikan oleh temannya, Pecorine. Namun, Kokoro adalah elf yang tidak suka dengan bilangan ganjil. Maka, dia ingin membagi buah apel untuk dirinya sendiri dan Pecorine dalam jumlah genap.

Bantulah Kokoro untuk mengetahui apakah n buah apel dapat dibagi menjadi 2 dengan hasil apel Kokoro dan Pecorine genap.

Jika n buah apel dapat dibagi dengan genap, keluarkan "Bisa". Jika tidak, maka keluarkan "Tidak".

Input Format

bagiApel(n)
Constraints

n: integer

Output Format

Bisa | Tidak
Sample Input 0

bagiApel(12)
Sample Output 0

Bisa
Explanation 0

Kokoro bisa membagi apel ke Pecorine dengan cara - (10, 2) - (8, 4) - (6, 6)

Sample Input 1

bagiApel(7)
Sample Output 1

Tidak
Explanation 1

Kokoro tidak bisa membagi 7 apel sebanyak genap ke dia sendiri dan Pecorine.
"""

def bagiApel(eval:int)->str:
    if eval % 2 == 0 and eval > 2:
        return("Bisa")
    else:
        return("Tidak")

#JANGAN DIUBAH!
print(eval(input()))