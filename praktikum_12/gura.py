def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def list_ke_bilangan(l):
    """
    Convert a list of digits to a number.

    :param l: The list of digits.
    :type l: list
    :return: The number represented by the list of digits.
    :rtype: int

    :example:
    >>> list_ke_bilangan([1, 2, 3])
    123

    :raises TypeError: If l is not a list.
    """
    if IsEmpty(l):
        return 0
    else:
        if IsOneElmt(l):
            return FirstElmt(l)
        else:
            if type(FirstElmt(l)) != int:
                return -1 * (list_ke_bilangan(Tail(l)))
            else:
                return FirstElmt(l) * 10 ** (NbElmt(l) - 1) + list_ke_bilangan(Tail(l))

def bilangan_ke_list(l):
    """
    Convert a number to a list of digits.

    :param l: The number.
    :type l: int
    :return: The list of digits representing the number.
    :rtype: list

    :example:
    >>> bilangan_ke_list(123)
    [1, 2, 3]

    :raises TypeError: If l is not an integer.
    """
    if l == 0:
        return []
    else:
        return bilangan_ke_list(l // 10) + [l % 10]

def shrimp(x, y):
    """
    Add two numbers represented as lists of digits.

    :param x: The first list of digits.
    :type x: list
    :param y: The second list of digits.
    :type y: list
    :return: The sum of the two numbers as a list of digits.
    :rtype: list

    :example:
    >>> shrimp([1, 2, 3], [4, 5, 6])
    [5, 7, 9]

    :raises TypeError: If x or y is not a list.
    """
    if (list_ke_bilangan(x) + list_ke_bilangan(y)) < 0:
        return ['-'] + bilangan_ke_list((list_ke_bilangan(x) + list_ke_bilangan(y)) * -1)
    elif (list_ke_bilangan(x) + list_ke_bilangan(y)) == 0:
        return [0]
    else:
        return bilangan_ke_list(list_ke_bilangan(x) + list_ke_bilangan(y))

if __name__ == "__main__":
    # Examples for NbElmt function
    print(NbElmt([1, 2, 3]))
    print(NbElmt([]))

    # Examples for list_ke_bilangan function
    print(list_ke_bilangan([1, 2, 3]))
    print(list_ke_bilangan([1, '2', 3]))

    # Examples for bilangan_ke_list function
    print(bilangan_ke_list(123))
    print(bilangan_ke_list(0))

    # Examples for shrimp function
    print(shrimp([1, 2, 3], [4, 5, 6]))
    print(shrimp([1, 2, 3], [-4, -5, -6]))