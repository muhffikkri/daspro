def is_triangle(side_1: int, side_2: int, side_3: int) -> bool:
    """
    Return True if the sides form a triangle, False otherwise. A triangle is valid if the sum of any two sides is greater than the third side.

    :param side_1: The length of the first side.
    :type side_1: int
    :param side_2: The length of the second side.
    :type side_2: int
    :param side_3: The length of the third side.
    :type side_3: int
    :return: True if the sides form a triangle, False otherwise.
    :rtype: bool

    :example:
    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(1, 1, 2)
    False
    """
    return side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2

def triangle_checker(side_1: int, side_2: int, side_3: int) -> str:
    """
    Return the type of triangle based on the lengths of its sides. If the sides do not form a triangle, return 'Not a triangle'.
    Otherwise, it depends on the side, if 3 side has the same length , return 'Equilateral', if 2 side has the same length, return 'Isosceles', if all side has different length, return 'Scalene'.

    :param side_1: The length of the first side.
    :type side_1: int
    :param side_2: The length of the second side.
    :type side_2: int
    :param side_3: The length of the third side.
    :type side_3: int
    :return: The type of triangle.
    :rtype: str

    :example:
    >>> triangle_checker(1, 1, 1)
    'Equilateral'
    >>> triangle_checker(1, 1, 2)
    'Isoceles'
    >>> triangle_checker(3, 2, 1)
    'Scalene'
    >>> triangle_checker(15, 20, 1)
    "That's not a triangle"
    """
    if is_triangle(side_1, side_2, side_3):
        if side_1 == side_2 == side_3:
            return "Equilateral"
        if side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
            return "Isoceles"
        return "Scalene"
    else :
        return "That's not a triangle"

if __name__ == "__main__":
    print(triangle_checker(1, 1, 1))  # Output: Equilateral
    print(triangle_checker(1, 1, 2))  # Output: Isoceles
    print(triangle_checker(3, 2, 1))  # Output: Scalene
    print(triangle_checker(15, 20, 1))  # Output: That's not a triangle