"""
You are tasked with calculating the mean of four numbers after removing the smallest and largest values. This is known as the "Olympic mean." The function MO(i, j, k, l, procedure) will compute this mean using one of two procedures. If procedure is 1, it uses separate functions to find the minimum and maximum values. If procedure is 2, it uses lambda functions to achieve the same result.

Input Format
MO(i, j, k, l, procedure)

Constraints
-1000 ≤ i, j, k, l ≤ 1000
procedure ∈ {1, 2}

Output Format
The Olympic mean of the four numbers.

Sample Input 0
MO(3, 5, 4, 2, 1)
Sample Output 0
3.5

Sample Input 1
MO(2, 2, 2, 2, 1)
Sample Output 1
2.0
"""

def min4(a: int, b: int, c: int, d: int) -> int:
    """
    Return the minimum of four numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :param c: The third number.
    :type c: int
    :param d: The fourth number.
    :type d: int
    :return: The minimum of the four numbers.
    :rtype: int
    """
    return min(a, b, c, d)

def max4(a: int, b: int, c: int, d: int) -> int:
    """
    Return the maximum of four numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :param c: The third number.
    :type c: int
    :param d: The fourth number.
    :type d: int
    :return: The maximum of the four numbers.
    :rtype: int
    """
    return max(a, b, c, d)

def minmax4(a: int, b: int, c: int, d: int, func) -> int:
    """
    Return the result of applying a function to four numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :param c: The third number.
    :type c: int
    :param d: The fourth number.
    :type d: int
    :param func: The function to apply.
    :type func: function
    :return: The result of applying the function to the four numbers.
    :rtype: int
    """
    return func(func(a, b), func(c, d))

def MO(i: int, j: int, k: int, l: int, procedure: int) -> float:
    """
    Calculate the Olympic mean of four numbers after removing the smallest and largest values.

    :param i: The first number.
    :type i: int
    :param j: The second number.
    :type j: int
    :param k: The third number.
    :type k: int
    :param l: The fourth number.
    :type l: int
    :param procedure: The procedure to use (1 or 2).
    :type procedure: int
    :return: The Olympic mean of the four numbers.
    :rtype: float

    :example:
    >>> MO(3, 5, 4, 2, 1)
    3.5
    >>> MO(2, 2, 2, 2, 1)
    2.0

    :raises ValueError: If procedure is not 1 or 2.
    """
    if procedure == 1:
        # Implementation using separate function
        return (i + j + k + l - min4(i, j, k, l) - max4(i, j, k, l)) / 2
    elif procedure == 2:
        # Implementation using lambda function
        return (i + j + k + l - minmax4(i, j, k, l, lambda x, y: x if x < y else y) - minmax4(i, j, k, l, lambda x, y: x if x > y else y)) / 2
    else:
        raise ValueError("Invalid procedure: must be 1 or 2")

if __name__ == "__main__":
    print(MO(3, 5, 4, 2, 1))  # Output: 3.5
    print(MO(2, 2, 2, 2, 1))  # Output: 2.0
    print(MO(-100, 100, 0, 50, 1))  # Output: 25.0
    print(MO(1, 2, 3, 4, 1))  # Output: 2.5
    print(MO(10, 20, 30, 40, 1))  # Output: 25.0