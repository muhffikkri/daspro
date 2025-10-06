# File Name: latihanB.py
# Description: Create recursive functions
# Author: Muhammad Fikri-24060124130069
# Date: October 1, 2024

def multiple_three_series(n: int) -> int:
    """
    Calculate the nth term of the series where each term is a multiple of three.

    :param n: The term position in the series.
    :type n: int
    :return: The nth term of the series.
    :rtype: int

    :example:
    >>> multiple_three_series(5)
    15

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return 3 if n == 1 else 3 + multiple_three_series(n - 1)

def real_number_series(n: int) -> int:
    """
    Calculate the sum of the first n real numbers.

    :param n: The number of terms to sum.
    :type n: int
    :return: The sum of the first n real numbers.
    :rtype: int

    :example:
    >>> real_number_series(5)
    15

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return n if n == 0 else n + real_number_series(n - 1)

def sum_of_multiple_three_series(n: int) -> int:
    """
    Calculate the sum of the first n terms of the series where each term is a multiple of three.

    :param n: The number of terms to sum.
    :type n: int
    :return: The sum of the first n terms of the series.
    :rtype: int

    :example:
    >>> sum_of_multiple_three_series(3)
    18

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return 3 if n == 1 else 3 * n + sum_of_multiple_three_series(n - 1)

def sum_of_three_power_n_series(n: int) -> int:
    """
    Calculate the sum of the series where each term is 3 raised to the power of (n-1).

    :param n: The number of terms to sum.
    :type n: int
    :return: The sum of the series.
    :rtype: int

    :example:
    >>> sum_of_three_power_n_series(3)
    13

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return 1 if n == 1 else 3 ** (n - 1) + sum_of_three_power_n_series(n - 1)

def sum_of_square_series(n: int) -> int:
    """
    Calculate the sum of the series where each term is the square of its position.

    :param n: The number of terms to sum.
    :type n: int
    :return: The sum of the series.
    :rtype: int

    :example:
    >>> sum_of_square_series(3)
    14

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return 1 if n == 1 else n**2 + sum_of_square_series(n - 1)

if __name__ == "__main__":
    # Examples that will only run when this file is executed directly
    print(multiple_three_series(5))  # Output: 15
    print(real_number_series(5))  # Output: 15
    print(sum_of_multiple_three_series(3))  # Output: 18
    print(sum_of_three_power_n_series(3))  # Output: 13
    print(sum_of_square_series(3))  # Output: 14