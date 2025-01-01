def sum_of_even(n: int) -> int:
    """
    Calculate the sum of the first n even numbers.

    :param n: The number of even numbers to sum.
    :type n: int
    :return: The sum of the first n even numbers.
    :rtype: int

    :example:
    >>> sum_of_even(1)
    2
    >>> sum_of_even(2)
    6
    >>> sum_of_even(3)
    12

    :raises TypeError: If n is not an integer.
    :raises ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    return (n // 2) * ((n // 2) + 1)

if __name__ == "__main__" : 
    print(sum_of_even(1))
    print(sum_of_even(2))
    print(sum_of_even(3))
    print(sum_of_even(4))
    print(sum_of_even(6))