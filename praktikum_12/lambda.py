def Konso(e, L) : 
    return [e] + L

def Konsi(L, e) :
    return L + [e]

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

def Head(L) :
    return L[:-1]

"""
lambda di notasi fungsional sebenarnya adalah sebuah fungsi callback. fungsi ini akan menjadi argumen dari fungsi lainnya. 

jika dianalogikan, misalnya kita memiliki sebuah wadah bohlam lampu dan kita memiliki bohlam yang berwarna merah, birum hijau. Wadah ini diibaratkan sebagai sebuah fungsi untuk menyalakan bohlam (tergantung bohlam apa yang kita pasang ke wadah), sedangkan bohlam diibaratkan sebagai lambda yang kita masukkan ke wadah (fungsi). Kita bebas untuk mengganti bohlam menjadi warna apapun yang kita inginkan. Fungsi hanya menjadi wadah untuk lambda yang kita masukkan.

Analogi yang lain adalah filter genap dan ganjil. Kita bisa membuat satu fungsi yang bisa menampung filter genap dan ganjil tergantung pada argumen yang kita masukkan. 

misalnya kita punya sebuah fungsi filter yang bisa filter genap atau ganjil




"""

lambda_1 = lambda x,y : x + y
lambda_2 = lambda x,y : x * y

def contoh_lambda(fungsi, parameter_1, parameter_2) : 
    return fungsi(parameter_1, parameter_2)

"""
APLIKASI 
==> contoh_lambda(lambda x,y : x + y, 5, 6) ---> return 5 + 6 = 11
==> contoh_lambda(lambda x,y : x * y, 5, 6) ---> return 5 * 6 = 30



"""
