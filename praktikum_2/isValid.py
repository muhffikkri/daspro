"""
Di tengah perjalanan di luar angkasa yang sunyi, Kevin, seorang peneliti yang cermat, menerima laporan dari asistennya tentang nilai misterius dari suatu objek yang baru ditemukan. Data tersebut berupa sebuah bilangan bulat, dan kini Kevin harus segera menentukan apakah objek tersebut aman atau berpotensi berbahaya. Untuk itu, ia memintamu membuat sebuah fungsi yang bisa membantu dalam pengambilan keputusan krusial ini. Dengan sigap, kamu merancang fungsi is_valid(x), yang dengan cepat dapat mengevaluasi keamanan objek tersebut. Fungsi ini akan memeriksa apakah nilai objek lebih kecil dari 5 atau lebih besar dari 500. Jika salah satu kondisi terpenuhi, objek dinyatakan aman, dan Kevin dapat melanjutkan penelitiannya dengan tenang. Jika tidak, Kevin tahu bahwa objek ini perlu diperiksa lebih lanjut untuk menghindari potensi bahaya di tengah gelapnya luar angkasa!

Input Format
is_valid(x)

Constraints
-1000 ≤ x ≤ 1000

Output Format
True / False

Sample Input 0
is_valid(4)
Sample Output 0
True

Sample Input 1
is_valid(10)
Sample Output 1
False
"""

def is_valid(x: float) -> bool :
    """Return true if x less than five and x greater than five hundred"""
    return x < 5 or x > 500

if __name__ == "__main__" : 
    print(is_valid(5)) # Output : False
    print(is_valid(7)) # Output : False
    print(is_valid(1)) # Output : True
    print(is_valid(35)) # Output : False