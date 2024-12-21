from typing import Callable

def square(x: int) -> int:
    """
    Return x squared.

    :param x: The number to be squared.
    :type x: int
    :return: The square of x.
    :rtype: int
    """
    return x * x

def square_root(x: int) -> float:
    """
    Return the square root of x.

    :param x: The number to find the square root of.
    :type x: int
    :return: The square root of x.
    :rtype: float
    """
    return x ** 0.5

def discriminant(a: int, b: int, c: int) -> float:
    """
    Return the discriminant of the quadratic equation ax^2 + bx + c = 0.

    :param a: Coefficient of x^2.
    :type a: int
    :param b: Coefficient of x.
    :type b: int
    :param c: Constant term.
    :type c: int
    :return: The discriminant of the quadratic equation.
    :rtype: float
    """
    return square(b) - 4 * a * c

def roots(a: int, b: int, c: int, func: Callable[[int, float], float]) -> float:
    """
    Return one of the roots of the quadratic equation ax^2 + bx + c = 0 using the provided function.

    :param a: Coefficient of x^2.
    :type a: int
    :param b: Coefficient of x.
    :type b: int
    :param c: Constant term.
    :type c: int
    :param func: A function that takes two arguments (int, float) and returns a float.
    :type func: Callable[[int, float], float]
    :return: One of the roots of the quadratic equation.
    :rtype: float
    """
    return func(-b, square_root(discriminant(a, b, c))) / (2 * a)

def roots_1(a: int, b: int, c: int) -> float:
    """
    Return one of the roots of the quadratic equation ax^2 + bx + c = 0.

    :param a: Coefficient of x^2.
    :type a: int
    :param b: Coefficient of x.
    :type b: int
    :param c: Constant term.
    :type c: int
    :return: One of the roots of the quadratic equation.
    :rtype: float
    """
    return (-b + square_root(discriminant(a, b, c))) / (2 * a)

def roots_2(a: int, b: int, c: int) -> float:
    """
    Return one of the roots of the quadratic equation ax^2 + bx + c = 0.

    :param a: Coefficient of x^2.
    :type a: int
    :param b: Coefficient of x.
    :type b: int
    :param c: Constant term.
    :type c: int
    :return: One of the roots of the quadratic equation.
    :rtype: float
    """
    return (-b - square_root(discriminant(a, b, c))) / (2 * a)

def division_between_2_square_roots(a: int, b: int, c: int, procedure: int) -> float:
    """
    Return 0 if the discriminant is negative, otherwise return the division between the two roots of the quadratic equation.
    The greater root divides the smaller one.

    :param a: Coefficient of x^2.
    :type a: int
    :param b: Coefficient of x.
    :type b: int
    :param c: Constant term.
    :type c: int
    :param procedure: The procedure to be used to calculate the roots. It can be 1 or 2.
    :type procedure: int
    :return: The division of the two roots.
    :rtype: float

    :raises ValueError: If a is 0.

    :example:
    >>> division_between_2_square_roots(1, -3, 2, 1)
    2.0
    >>> division_between_2_square_roots(1, -3, 2, 2)
    2.0
    """
    if a == 0:
        raise ValueError("Invalid input: a is 0")

    if discriminant(a, b, c) < 0:
        return 0

    if procedure == 1:
        root1 = roots_1(a, b, c)
        root2 = roots_2(a, b, c)
    elif procedure == 2:
        root1 = roots(a, b, c, lambda x, y: x + y)
        root2 = roots(a, b, c, lambda x, y: x - y)
    else:
        raise ValueError("Invalid procedure: must be 1 or 2")

    return max(root1, root2) / min(root1, root2)

if __name__ == "__main__":
    print(division_between_2_square_roots(1, -3, 2, 1))  # Output: 2.0
    print(division_between_2_square_roots(1, -3, 2, 2))  # Output: 2.0
    print(division_between_2_square_roots(1, -4, 4, 2))  # Output: 2.0
    print(division_between_2_square_roots(0, 2, 3, 1))  # Output: ValueError: Invalid input: a is 0
    print(division_between_2_square_roots(1, -3, 2, 3))  # Output: ValueError: Invalid procedure: must be 1 or 2
