from typing import Callable

"""
Di tengah kerasnya petualangan di Antartika, Sandy, seorang petualang tangguh, tiba-tiba merasa bosan dengan dinginnya es dan salju. Untuk mengusir kebosanan, Sandy mengajukan tantangan menarik: "Coba buatkan aku sebuah fungsi yang bisa menghitung rata-rata dari angka-angka, tapi bukan sembarang rata-rata—aku ingin yang istimewa! Hitung rata-rata dari bilangan yang bukan yang terbesar dan bukan yang terkecil!"Dengan semangat, kamu menciptakan fungsi MO(a, b, c, d), sebuah formula ajaib yang secara cerdik memilih dua bilangan di antara empat angka yang diberikan, mengabaikan yang paling besar dan yang paling kecil. Hasilnya? Sandy pun terkesima melihat angka yang muncul, sebuah rata-rata yang sempurna untuk menemani petualangan berikutnya di tengah daratan es yang tak kenal ampun!

Input Format
MO(a,b,c,d)

Constraints
-100 ≤ a,b,c,d ≤ 100

Output Format
x

Sample Input 0
MO(3,5,4,2)
Sample Output 0

3.5
Sample Input 1
MO(2,2,2,2)
Sample Output 1
2.0
"""

def min2(i: float, j: float) -> float : 
    """Return the smaller of i and j"""
    return (i + j - abs(i - j)) / 2

def max2(i: float, j: float) -> float : 
    """Return the greater of i, and j"""
    return (i + j + abs(i - j)) / 2

def min4(i: float, j: float, k: float, l: float) -> float : 
    """Return the smaller of i, j, k, and, l"""
    return min2(min2(i, j), min2(k, l))

def max4(i: float, j: float, k: float, l: float) -> float : 
    """Return the greater of i, j, k, and, l"""
    return max2(max2(i, j), max2(k, l))

def minmax2(i: float, j: float, f: callable) : 
    """Return the smaller of i and j, or the result of applying function f to i and
    j, whichever is smaller"""
    return f(i, j)

def minmax4(i: float, j: float, k: float, l: float, f: callable) -> float : 
    """Return the smaller of i and j, or the result of applying function f to i and
    j, whichever is smaller
    """
    return minmax2(minmax2(i, j, f), minmax2(k, l, f))


def MO(i: float, j: float, k: float, l: float, procedure: int) -> float :
    """
    Calculate the mean of four numbers excluding the highest and lowest values.

    :param i: The first number.
    :type i: int
    :param j: The second number.
    :type j: int
    :param k: The third number.
    :type k: int
    :param l: The fourth number.
    :type l: int
    :param procedure: Choose Procedure for the return value
    :type procedure: int
    :return: The mean of the two middle numbers.
    :rtype: float

    :example:
    >>> MO(3, 5, 4, 2)
    3.5

    :raises TypeError: If any of the inputs is not an integer.
    """

    if procedure == 1 : 
        # Implementation using separate function
        return (i + j + k + l - min4(i, j, k, l) - max4(i, j, k, l)) / 2
    elif procedure == 2 : 
        # Implementation using lambda function
        return (i + j + k + l - minmax4(i, j, k, l, lambda x,y: x if x<y else y) - minmax4(lambda x,y: x if x>y else y)) / 2
    else : 
        raise ValueError("Invalid rocedure: must be 1 or 2")
    
if __name__ == "__main__" : 
    print(MO(3, 5, 4, 2, 1)) # Output: 3.5
    print(MO(2, 2, 2, 2, 1)) # Output: 2.0
    print(MO(-100, 100, 0, 50, 1)) # Output 25.0
    print(MO(1, 2, 3, 4, 1)) # Output: 2.5
    print(MO(10, 20, 30, 40, 1)) # Output: 25.0