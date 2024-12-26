"""
Xaviera, an adventurer who loves exploring maps and measuring distances between places she discovers, gives you an interesting challenge. She provides two coordinate points on the Cartesian plane, (x1, y1) and (x2, y2), and asks you to calculate the distance between these two points. This distance will help her determine how far she needs to travel to her next adventure. With enthusiasm, you create the function least_square(x1, y1, x2, y2), which uses the magical formula from geometry, the Euclidean distance formula. This function will calculate the shortest distance between the two points on the Cartesian plane, giving Xaviera the information she needs to continue her journey. With each step she takes, Xaviera will know exactly how far she has traveled, thanks to the distance calculation you performed!

Input Format
least_square(x1, y1, x2, y2)

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

def square(x: float) -> float:
    """
    Return the square of x.

    :param x: The number to be squared.
    :type x: float
    :return: The square of x.
    :rtype: float
    """
    return x * x

def square_root(x: float) -> float:
    """
    Return the square root of x.

    :param x: The number to find the square root of.
    :type x: float
    :return: The square root of x.
    :rtype: float
    """
    return x ** 0.5

def least_square(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).

    :param x1: The x-coordinate of the first point.
    :type x1: float
    :param y1: The y-coordinate of the first point.
    :type y1: float
    :param x2: The x-coordinate of the second point.
    :type x2: float
    :param y2: The y-coordinate of the second point.
    :type y2: float
    :return: The Euclidean distance between the two points.
    :rtype: float

    :example:
    >>> least_square(0, 0, 3, 4)
    5.0
    >>> least_square(1, 2, 4, 6)
    5.0

    :raises TypeError: If any of the coordinates are not floats.
    """
    if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2]):
        raise TypeError("All coordinates must be numbers")
    return square_root(square(x2 - x1) + square(y2 - y1))

if __name__ == "__main__":
    print(least_square(0, 0, 3, 4))  # Output: 5.0
    print(least_square(1, 2, 4, 6))  # Output: 5.0
    print(least_square(-1, -1, 1, 1)) # Output: 2.8284271247461903
    print(least_square(2, 3, 5, 7)) # Output: 5.0
