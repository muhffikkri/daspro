"""
Maxwell, with his peculiar yet charming uniqueness, has a very specific fondness for the letter 'a'. No other character can capture his attention like 'a'—not 'y', and certainly not strange symbols like '@'. Therefore, he challenges you to create a function that can distinguish between 'a' and all other characters. Without hesitation, you create the function is_an_a(c), which ensures whether the given character is the star, 'a'. If the character is 'a', Maxwell will cheer with joy; however, if it is not, Maxwell will know that it is not his favorite!

Input Format
is_an_a(c)

Constraints
|c| = 1

Output Format
True / False

Sample Input 0
is_an_a('a')
Sample Output 0
True

Sample Input 1
is_an_a('@')
Sample Output 1
False
"""

def isAnA(c: str) -> bool:
    """
    Determine if the given character is 'a'.

    :param c: A single character to be checked.
    :type c: str
    :return: True if the character is 'a', False otherwise.
    :rtype: bool

    :example:
    >>> isAnA('a')
    True
    >>> isAnA('b')
    False

    :raises TypeError: If c is not a string or if its length is not 1.
    """
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("c must be a single character string")
    return c == 'a'

if __name__ == "__main__":
    print(isAnA("c")) # Output: False
    print(isAnA("g")) # Output: False
    print(isAnA("d")) # Output: False
    print(isAnA("a")) # Output: True