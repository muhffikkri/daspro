#  Example of a Well-Documented Function Here is an example of a well-documented function following the best practices:

def add(x: int, y: int) -> int:
    """
    Add two numbers and return the result.

    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :return: The sum of x and y.
    :rtype: int

    :example:
    >>> add(2, 3)
    5

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return x + y

if __name__ == "__main__" : 
    print(add(2, 3))
    print(add(2.5, 3))
    print(add(2, 3.5))
    print(add(2.5, 3.5))
    print(add(2, 3.5))
    print(add(2.5, 3))
    print(add(2.5, 3.5))