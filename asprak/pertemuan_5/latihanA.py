# File Name: latihanA.py
# Description: Create recursive functions
# Author: Muhammad Fikri-24060124130069
# Date: October 1, 2024

def faktorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    :param n: The number to calculate the factorial of.
    :type n: int
    :return: The factorial of n.
    :rtype: int

    :example:
    >>> faktorial(5)
    120

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return 1 if n == 1 else n * faktorial(n - 1)

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    :param n: The position in the Fibonacci sequence.
    :type n: int
    :return: The nth Fibonacci number.
    :rtype: int

    :example:
    >>> fibonacci(5)
    5

    :raises TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def tambah(x: int, y: int) -> int:
    """
    Add two numbers using recursion.

    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :return: The sum of x and y.
    :rtype: int

    :example:
    >>> tambah(5, 5)
    10

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return x if y == 0 else tambah(x, y - 1) + 1

def kurang(x: int, y: int) -> int:
    """
    Subtract two numbers using recursion.

    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :return: The result of x minus y.
    :rtype: int

    :example:
    >>> kurang(5, 5)
    0

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return x if y == 0 else kurang(x, y - 1) - 1

def bagi(x: int, y: int) -> int:
    """
    Divide two numbers using recursion.

    :param x: The dividend.
    :type x: int
    :param y: The divisor.
    :type y: int
    :return: The quotient of x divided by y.
    :rtype: int

    :example:
    >>> bagi(5, 5)
    1

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return 0 if x < y else 1 + bagi(x - y, y)

def pangkat(x: int, y: int) -> int:
    """
    Calculate the power of a number using recursion.

    :param x: The base.
    :type x: int
    :param y: The exponent.
    :type y: int
    :return: The result of x raised to the power of y.
    :rtype: int

    :example:
    >>> pangkat(5, 3)
    125

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return 1 if y == 0 else x * pangkat(x, y - 1)

def kali(x: int, y: int) -> int:
    """
    Multiply two numbers using recursion.

    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :return: The product of x and y.
    :rtype: int

    :example:
    >>> kali(5, 3)
    15

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    if y == 0: return 0
    elif y == 1: return x
    else: return x + kali(x, y - 1)

if __name__ == "__main__":
    # Examples that will only run when this file is executed directly
    print(faktorial(5))  # Output: 120
    print(fibonacci(5))  # Output: 5
    print(tambah(5, 5))  # Output: 10
    print(kurang(5, 5))  # Output: 0
    print(bagi(5, 5))    # Output: 1
    print(pangkat(5, 3)) # Output: 125
    print(kali(5, 3))    # Output: 15