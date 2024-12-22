# Nama File : latihanB.py
# Deskripsi : membuat fungsi rekursif
# Pembuat   : Muhammad Fikri-24060124130069
# Tanggal   : 01 Oktober 2024

def multiple_three_series(n) :
    return 3 if n == 1 else 3 + multiple_three_series(n - 1)

def real_number_series(n) :
    return n if n == 0 else n + real_number_series(n - 1)

def sum_of_multiple_three_series(n) : 
    return 3 if n == 1 else 3 * n + sum_of_multiple_three_series(n - 1)

def sum_of_three_power_n_series(n) :
    return 1 if n == 1 else 3 ** (n - 1) + sum_of_three_power_n_series(n - 1)

def sum_of_square_series(n) :
    return 1 if n == 1 else n**2 + sum_of_square_series(n - 1)

print(multiple_three_series(5))
print(real_number_series(5))
print(sum_of_multiple_three_series(3))
print(sum_of_three_power_n_series(3))
print(sum_of_square_series(3))