# File Name: point.py
# Description: Create a point type along with its constructor and selectors
# Author: Muhammad Fikri-24060124130069
# Date: September 24, 2024

from math import sqrt

# DEFINITION AND SPECIFICATION OF FUNCTION FX2
# fx2: integer --> integer
# {fx2(x) calculates the square of x}
# Realization in Python
def fx2(x):
    """
    Calculate the square of x.

    :param x: The number to be squared.
    :type x: int
    :return: The square of x.
    :rtype: int

    :example:
    >>> fx2(3)
    9

    :raises TypeError: If x is not an integer.
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    return x * x

# TYPE DEFINITION
# type point : <x:real, y:real>
# {<x, y> is a point, with x as the abscissa and y as the ordinate}

# DEFINITION AND SPECIFICATION OF CONSTRUCTOR
# MakePoint: 2 real --> point
# {MakePoint(x, y) forms a point from a and b with a as the abscissa and b as the ordinate}
# Realization in Python
def makePoint(a, b):
    """
    Create a point from two real numbers.

    :param a: The abscissa of the point.
    :type a: float
    :param b: The ordinate of the point.
    :type b: float
    :return: A point as a list [a, b].
    :rtype: list

    :example:
    >>> makePoint(3.0, 4.0)
    [3.0, 4.0]

    :raises TypeError: If a or b is not a float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be numbers")
    return [a, b]

# DEFINITION AND SPECIFICATION OF SELECTOR
# Absis: point --> real
# {Absis(P) returns the abscissa of point P}
# Realization in Python
def absis(P):
    """
    Return the abscissa of the point.

    :param P: The point.
    :type P: list
    :return: The abscissa of the point.
    :rtype: float

    :example:
    >>> absis([3.0, 4.0])
    3.0

    :raises TypeError: If P is not a list.
    """
    if not isinstance(P, list):
        raise TypeError("P must be a list")
    return P[0]

# Ordinat: point --> real
# {Ordinat(P) returns the ordinate of point P}
# Realization in Python
def ordinat(P):
    """
    Return the ordinate of the point.

    :param P: The point.
    :type P: list
    :return: The ordinate of the point.
    :rtype: float

    :example:
    >>> ordinat([3.0, 4.0])
    4.0

    :raises TypeError: If P is not a list.
    """
    if not isinstance(P, list):
        raise TypeError("P must be a list")
    return P[1]

# InfoPoint: point --> string
# {InfoPoint(P) memberikan informasi absis dan ordinat P}
# Realisasi dalam Python
def infoPoint(P):
    return f"Absis: {absis(P)}, Ordinat: {ordinat(P)}"

# DEFINITION AND SPECIFICATION OF OPERATOR
# Distance: 2 points --> real
# {Distance(P1, P2) calculates the distance between two points P1 and P2}
# Realization in Python
def distance(P1, P2):
    """
    Calculate the distance between two points.

    :param P1: The first point.
    :type P1: list
    :param P2: The second point.
    :type P2: list
    :return: The distance between the two points.
    :rtype: float

    :example:
    >>> distance([0, 0], [3, 4])
    5.0

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return sqrt(fx2(absis(P2) - absis(P1)) + fx2(ordinat(P2) - ordinat(P1)))

# JarakO: point --> real
# {JarakO(P) menghitung jarak antara P dengan titik origin (0, 0)}
# Realisasi dalam Python
def jarakO(P):
    return sqrt(
        fx2(absis(P) + ordinat(P))
    )

# Kuadran: point --> string
# {Kuadran(P) mengembalikan kuadran di mana point P berada, dengan syarat P bukan titik (0, 0) tidak terletak di sumbu X maupun sumbu Y}
# Realisasi dalam Python 
def kuadran(P):
    if(absis(P) > 0) : return "Kuadran 1" if ordinat(P) > 0 else "Kuadran 4"
    return "Kuadran 2" if ordinat(P) > 0 else "Kuadran 3"

# Midpoint: 2 points --> point
# {Midpoint(P1, P2) calculates the midpoint between two points P1 and P2}
# Realization in Python
def midpoint(P1, P2):
    """
    Calculate the midpoint between two points.

    :param P1: The first point.
    :type P1: list
    :param P2: The second point.
    :type P2: list
    :return: The midpoint between the two points.
    :rtype: list

    :example:
    >>> midpoint([0, 0], [4, 4])
    [2.0, 2.0]

    :raises TypeError: If P1 or P2 is not a list.
    """
    if not (isinstance(P1, list) and isinstance(P2, list)):
        raise TypeError("Both P1 and P2 must be lists")
    return makePoint((absis(P1) + absis(P2)) / 2, (ordinat(P1) + ordinat(P2)) / 2)

if __name__ == "__main__":
    # Examples that will only run when this file is executed directly
    P = makePoint(1, 2)
    Q = makePoint(4, 6)
    print(absis(P))  # Output: 1
    print(ordinat(P))  # Output: 2
    print(distance(P, Q))  # Output: 5.0
    print(midpoint(P, Q))  # Output: [2.5, 4.0]