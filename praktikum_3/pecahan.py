# File Name: pecahan_campuran.py
# Description: Create a mixed fraction type along with its constructor and selectors
# Author: Muhammad Fikri-24060124130069
# Date: October 11, 2024

# TYPE DEFINITION
# type pecahanc: <bil: integer, n:integer >= 0, d:integer > 0 >
# {<bil, n, d> is a mixed fraction, with bil as the integer part, n as the numerator, and d as the denominator. The numerator is always less than the denominator (n < d)}

# DEFINITION AND SPECIFICATION OF CONSTRUCTOR
# makePecahan: 3 integers --> pecahanc
# makePecahan(bil, n, d) forms an array from bil, n, and d with bil as the integer part, n as the numerator, and d as the denominator
# Realization of makePecahan function
def makePecahan(bil, n, d):
    """
    Create a mixed fraction from three integers.

    :param bil: The integer part of the fraction.
    :type bil: int
    :param n: The numerator of the fraction.
    :type n: int
    :param d: The denominator of the fraction.
    :type d: int
    :return: A mixed fraction as a list [bil, n, d].
    :rtype: list

    :example:
    >>> makePecahan(1, 2, 3)
    [1, 2, 3]

    :raises TypeError: If bil, n, or d is not an integer.
    """
    if not all(isinstance(i, int) for i in [bil, n, d]):
        raise TypeError("bil, n, and d must be integers")
    return [bil, n, d]

# pemb: pecahan --> int
# {pemb(P) returns the integer part of the fraction P}
# Realization of pemb function
def pemb(P):
    """
    Return the integer part of the fraction.

    :param P: The mixed fraction.
    :type P: list
    :return: The integer part of the fraction.
    :rtype: int

    :example:
    >>> pemb([1, 2, 3])
    1

    :raises TypeError: If P is not a list.
    """
    if not isinstance(P, list):
        raise TypeError("P must be a list")
    return P[0]

# peny: pecahan --> int
# {peny(P) returns the numerator of the fraction P}
# Realization of peny function
def peny(P):
    """
    Return the numerator of the fraction.

    :param P: The mixed fraction.
    :type P: list
    :return: The numerator of the fraction.
    :rtype: int

    :example:
    >>> peny([1, 2, 3])
    2

    :raises TypeError: If P is not a list.
    """
    if not isinstance(P, list):
        raise TypeError("P must be a list")
    return P[1]

# AddP: 2 fractions --> fraction
# {AddP(P1, P2) adds two fractions P1 and P2}
# Realization of AddP function
def AddP(P1, P2):
    """
    Add two fractions and return the result.

    :param P1: The first fraction.
    :type P1: list
    :param P2: The second fraction.
    :type P2: list
    :return: The sum of P1 and P2 as a fraction.
    :rtype: list

    :example:
    >>> AddP([1, 2, 3], [1, 3, 4])
    [1, 17, 12]

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return makePecahan(
        (pemb(P1) * peny(P2)) + (pemb(P2) * peny(P1)), 
        peny(P1) * peny(P2)
    )

# SubP: 2 fractions --> fraction
# {SubP(P1, P2) subtracts the second fraction from the first}
# Realization of SubP function
def SubP(P1, P2):
    """
    Subtract the second fraction from the first and return the result.

    :param P1: The first fraction.
    :type P1: list
    :param P2: The second fraction.
    :type P2: list
    :return: The difference of P1 and P2 as a fraction.
    :rtype: list

    :example:
    >>> SubP([1, 2, 3], [1, 3, 4])
    [1, 1, 12]

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return makePecahan(
        (pemb(P1) * peny(P2)) - (pemb(P2) * peny(P1)), 
        peny(P1) * peny(P2)
    )

# MulP: 2 fractions --> fraction
# {MulP(P1, P2) multiplies two fractions P1 and P2}
# Realization of MulP function
def MulP(P1, P2):
    """
    Multiply two fractions and return the result.

    :param P1: The first fraction.
    :type P1: list
    :param P2: The second fraction.
    :type P2: list
    :return: The product of P1 and P2 as a fraction.
    :rtype: list

    :example:
    >>> MulP([1, 2, 3], [1, 3, 4])
    [1, 6, 12]

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return makePecahan(
        pemb(P1) * pemb(P2),
        peny(P1) * peny(P2)
    )

# DivP: 2 fractions --> fraction
# {DivP(P1, P2) divides the first fraction by the second}
# Realization of DivP function
def DivP(P1, P2):
    """
    Divide the first fraction by the second and return the result.

    :param P1: The first fraction.
    :type P1: list
    :param P2: The second fraction.
    :type P2: list
    :return: The quotient of P1 and P2 as a fraction.
    :rtype: list

    :example:
    >>> DivP([1, 2, 3], [1, 3, 4])
    [1, 8, 9]

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return makePecahan(
        pemb(P1) * peny(P2),
        pemb(P2) * peny(P1)
    )

# REalP : 1 pecahan --> real
# {REalP (P) menuliskan pecahan dalam bentuk notasi desimal}
# Realisasi fungsi RealP
def RealP (P) :
    return pemb(P)/peny(P)
   
# IsEqP : 2 pecahan --> boolean
# {IsEqP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 sama dengan P2}
# Realisasi fungsi IsEqP
def IsEqP (P1,P2) :
    return pemb(P1) == pemb(P2) and peny(P1) == peny(P2)
   
# IsLtP : 2 pecahan --> boolean
# {IsLtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih kecil P2}
# Realisasi fungsi IsLtP
def IsLtP (P1,P2) :
    return True if(pemb(P1) * peny(P2) < pemb(P2) * peny(P1)) else False
   
# IsGtP : 2 pecahan --> boolean
# {IsGtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih besar P2}
# Realisasi fungsi IsGtP
def IsGtP (P1,P2) :
   return True if(pemb(P1) * peny(P2) > pemb(P2) * peny(P1)) else False

#APLIKASI
if __name__ == "__main__" : 
    P = makePecahan (1,2)
    Q = makePecahan (1,2)
    print (pemb(P)) # --> 1
    print (peny(P)) # --> 2
    print (AddP (P,Q)) # --> [4, 4]
    print (SubP (P,Q)) # --> [0, 4]
    print (MulP (P,Q)) # --> [1, 4]
    print (DivP (P,Q)) # --> [2, 2]
    print (RealP (P)) # --> 0.5
    print (IsEqP (P,Q)) # --> True
    print (IsLtP (P,Q)) # --> False
    print (IsGtP (P,Q)) # --> False