"""
In the midst of a quiet space journey, Kevin, a meticulous researcher, receives a report from his assistant about the mysterious value of a newly discovered object. The data is an integer, and now Kevin must quickly determine whether the object is safe or potentially dangerous. To do this, he asks you to create a function that can help make this crucial decision. Promptly, you design the function is_valid(x), which can quickly evaluate the safety of the object. This function will check if the object's value is less than 5 or greater than 500. If either condition is met, the object is declared safe, and Kevin can continue his research with peace of mind. If not, Kevin knows that this object needs further examination to avoid potential danger in the dark expanse of space!

Input Format
is_valid(x)

Constraints
-1000 ≤ x ≤ 1000

Output Format
True / False

Sample Input 0
is_valid(4)
Sample Output 0
True

Sample Input 1
is_valid(10)
Sample Output 1
False
"""

def is_valid(x: int) -> bool:
    """
    Determine if the given value is safe based on the specified conditions.

    :param x: The value of the object to be checked.
    :type x: int
    :return: True if the value is less than 5 or greater than 500, False otherwise.
    :rtype: bool

    :example:
    >>> is_valid(4)
    True
    >>> is_valid(10)
    False

    :raises TypeError: If x is not an integer.
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    return x < 5 or x > 500

if __name__ == "__main__":
    print(is_valid(5))  # Output: False
    print(is_valid(7))  # Output: False
    print(is_valid(1))  # Output: True
    print(is_valid(35)) # Output: False