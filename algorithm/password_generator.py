import random

char_lowercase = list(range(97, 123))
char_uppercase = list(range(65, 91))
char_number = list(range(48, 58))
char_symbol = list(range(33, 48)) + list(range(58, 65))
all_chars = char_lowercase + char_uppercase + char_number + char_symbol

def password_generator(length: int) -> str:
    """
    Generate a random password of a given length.

    :param length: The length of the password to be generated.
    :type length: int
    :return: A randomly generated password.
    :rtype: str

    :example:
    >>> password_generator(5)
    'aB3$d'

    :raises ValueError: If length is not a positive integer.
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be a positive integer")

    password = ''.join(random.choices([chr(c) for c in all_chars], k=length))
    
    return password

if __name__ == "__main__":
    print(password_generator(5))
