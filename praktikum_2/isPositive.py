"""
Maxwell, a number wizard with a special interest in positive numbers, asks you to create a magical spell. He says, "Create a function that can tell me if a number is one of my favorites or not. Remember, I like all positive numbers—and yes, even the number 0!" With the speed of a skilled programmer, you create the function is_positif(x), which can easily detect if a number is on Maxwell's favorite list. If the number is greater than or equal to zero, Maxwell will smile broadly, because it is his favorite number!

Input Format
is_positif(x)

Constraints
-100 ≤ x ≤ 100

Output Format
True / False

Sample Input 0
is_positif(1)
Sample Output 0
True

Sample Input 1
is_positif(-1)
Sample Output 1
False
"""

def is_positif(x: float) -> bool:
    """
    Determine if the given number is positive or zero.

    :param x: The number to be checked.
    :type x: float
    :return: True if the number is positive or zero, False otherwise.
    :rtype: bool

    :example:
    >>> is_positif(1)
    True
    >>> is_positif(-1)
    False

    :raises TypeError: If x is not a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    return x >= 0

if __name__ == "__main__":
    print(is_positif(5))  # Output: True
    print(is_positif(1))  # Output: True
    print(is_positif(-5)) # Output: False
    print(is_positif(7))  # Output: True
    print(is_positif(2))  # Output: True