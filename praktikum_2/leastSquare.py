"""
Xaviera, seorang petualang yang suka menjelajah peta dan mengukur jarak antara tempat-tempat yang ia temukan, memberimu sebuah tantangan menarik. Dia memberikan dua titik koordinat pada bidang kartesius, (x1, y1) dan (x2, y2), dan memintamu untuk menghitung jarak antara kedua titik tersebut. Jarak ini akan membantunya menentukan seberapa jauh ia harus melangkah menuju petualangan berikutnya. Dengan semangat, kamu menciptakan fungsi least_square(x1, y1, x2, y2), yang menggunakan formula ajaib dari geometri, yaitu rumus jarak Euclidean. Fungsi ini akan menghitung jarak terpendek antara kedua titik tersebut di bidang kartesius, memberi Xaviera informasi yang ia butuhkan untuk melanjutkan perjalanannya. Dengan setiap langkah yang ia ambil, Xaviera akan tahu pasti seberapa jauh ia telah berjalan, berkat perhitungan jarak yang kamu lakukan!

Input Format
least_square(x1,y1,x2,y2)

Constraints
-100 ≤ x1, y1, x2, y2 ≤ 100

Output Format
x

Sample Input 0
least_square(0,0,3,4)
Sample Output 0
5.0

Sample Input 1
least_square(1, 2, 4, 6)
Sample Output 1
5.0
"""

def square(x: float) -> float :
    """Return square of x"""
    return x*x

def square_root(x: float) -> float : 
    """Return square root of x"""
    return x**0.5
    
def least_square(x1: float, y1: float, x2: float, y2: float) -> float :
    """Return the norm of (x1, y1) and (x2, y2)"""
    return square_root(square(x2 - x1) + square(y2 - y1))

if __name__ == "__main__" : 
    print(least_square(0, 0, 3, 4)) # Output: 5.0
    print(least_square(1, 2, 4, 6)) # Output: 5.0
    print(least_square(-1, -1, 1, 1)) # Output: 2.8284271247461903
    print(least_square(2, 3, 5, 7)) # Output: 5.0
