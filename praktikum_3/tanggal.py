# File Name: tanggal.py
# Description: Create a date type along with its constructor and selectors
# Author: Muhammad Fikri-24060124130069
# Date: September 24, 2024

# TYPE DEFINITION
# type tanggal : <x:integer, y:integer, z:integer>
# {<x, y, z> is a date, with x as the day, y as the month, and z as the year}

# DEFINITION AND SPECIFICATION OF CONSTRUCTOR
# makeTanggal: 3 integers --> tanggal
# makeTanggal(x, y, z) forms an array from x, y, and z with x as the day, y as the month, and z as the year
# Realization of makeTanggal function
def makeTanggal(x, y, z):
    """
    Create a date from three integers.

    :param x: The day.
    :type x: int
    :param y: The month.
    :type y: int
    :param z: The year.
    :type z: int
    :return: A date as a list [x, y, z].
    :rtype: list

    :example:
    >>> makeTanggal(24, 9, 2024)
    [24, 9, 2024]

    :raises TypeError: If x, y, or z is not an integer.
    """
    if not all(isinstance(i, int) for i in [x, y, z]):
        raise TypeError("x, y, and z must be integers")
    return [x, y, z]

# tanggal: tanggal --> integer
# {tanggal(arr) returns the day component of the date arr}
# Realization of tanggal function
def tanggal(arr):
    """
    Return the day component of the date.

    :param arr: The date.
    :type arr: list
    :return: The day component of the date.
    :rtype: int

    :example:
    >>> tanggal([24, 9, 2024])
    24

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[0]

# bulan: tanggal --> integer
# {bulan(arr) returns the month component of the date arr}
# Realization of bulan function
def bulan(arr):
    """
    Return the month component of the date.

    :param arr: The date.
    :type arr: list
    :return: The month component of the date.
    :rtype: int

    :example:
    >>> bulan([24, 9, 2024])
    9

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[1]

# tahun: tanggal --> integer
# {tahun(arr) returns the year component of the date arr}
# Realization of tahun function
def tahun(arr):
    """
    Return the year component of the date.

    :param arr: The date.
    :type arr: list
    :return: The year component of the date.
    :rtype: int

    :example:
    >>> tahun([24, 9, 2024])
    2024

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[2]

if __name__ == "__main__":
    # Examples that will only run when this file is executed directly
    print(makeTanggal(24, 9, 2024))  # Output: [24, 9, 2024]
    print(tanggal([24, 9, 2024]))    # Output: 24
    print(bulan([24, 9, 2024]))      # Output: 9
    print(tahun([24, 9, 2024]))      # Output: 2024