"""
Imagine you are thrown into a magical isekai world, where everything can be represented on a two-dimensional Cartesian plane. In this world, you always know exactly where you are, complete with coordinates. One day, you wonder if you are at the starting point of all these adventures, which is the origin (0,0). With the spirit of a true adventurer, you create a function called is_origin(x, y), which will easily tell you whether you are standing at the zero point of this isekai world, or if you still have to explore further!

Input Format

is_origin(x, y)

Constraints

-100 ≤ x, y ≤ 100

Output Format

True or False

Sample Input 0
>>> is_origin(0,0)
Sample Output 0
True

Sample Input 1
>>> is_origin(1,1)
Sample Output 1
False
"""

def is_origin(x: float, y: float) -> bool:
    """
    Determine if the given coordinates (x, y) are at the origin (0, 0).

    :param x: The x-coordinate.
    :type x: float
    :param y: The y-coordinate.
    :type y: float
    :return: True if the coordinates are at the origin, False otherwise.
    :rtype: bool

    :example:
    >>> is_origin(0, 0)
    True
    >>> is_origin(1, 1)
    False

    :raises TypeError: If x or y is not a float.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numbers")
    return x == 0 and y == 0

if __name__ == "__main__":
    print(is_origin(3, 4))  # Output: False
    print(is_origin(1, 9))  # Output: False
    print(is_origin(0, 0))  # Output: True