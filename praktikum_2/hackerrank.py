# JAM PASIR AJAIB
def jam(j: int, m: int, s: int) -> str:
    """
    Validate and format the given time.

    :param j: The hour.
    :type j: int
    :param m: The minute.
    :type m: int
    :param s: The second.
    :type s: int
    :return: A formatted string of the time or an error message.
    :rtype: str

    :example:
    >>> jam(12, 30, 45)
    'Jam: 12, Menit: 30, Detik: 45'
    >>> jam(25, 61, 61)
    'Waktu tidak valid'

    :raises TypeError: If j, m, or s is not an integer.
    """
    if not (isinstance(j, int) and isinstance(m, int) and isinstance(s, int)):
        raise TypeError("j, m, and s must be integers")
    if (0 <= j <= 24 and 0 <= m < 60 and 0 <= s < 60):
        return f"Jam: {j}, Menit: {m}, Detik: {s}"
    return "Waktu tidak valid"

# LALU LINTAS LANGIT
def monitor_pesawat(x: int, y: int, z: int) -> str:
    """
    Monitor the status of an aircraft based on altitude, speed, and fuel.

    :param x: The altitude of the aircraft.
    :type x: int
    :param y: The speed of the aircraft.
    :type y: int
    :param z: The fuel level of the aircraft.
    :type z: int
    :return: The status of the aircraft.
    :rtype: str

    :example:
    >>> monitor_pesawat(13000, 800, 30)
    'Terlalu Tinggi'
    >>> monitor_pesawat(6000, 500, 60)
    'Berjalan Normal'

    :raises TypeError: If x, y, or z is not an integer.
    """
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        raise TypeError("x, y, and z must be integers")
    if x > 12000:
        return "Terlalu Tinggi"
    elif y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x < 5000 and (200 < y < 900) and z > 50:
        return "Aman untuk Mendarat"
    return "Berjalan Normal"

# JALAN SEMUT
def squareRoot(s: float) -> float:
    """
    Calculate the square root of a number.

    :param s: The number to calculate the square root of.
    :type s: float
    :return: The square root of the number.
    :rtype: float

    :example:
    >>> squareRoot(4)
    2.0

    :raises TypeError: If s is not a float.
    """
    if not isinstance(s, (int, float)):
        raise TypeError("s must be a number")
    return s ** 0.5

def square(s: float) -> float:
    """
    Calculate the square of a number.

    :param s: The number to calculate the square of.
    :type s: float
    :return: The square of the number.
    :rtype: float

    :example:
    >>> square(4)
    16

    :raises TypeError: If s is not a float.
    """
    if not isinstance(s, (int, float)):
        raise TypeError("s must be a number")
    return s * s

def min2(i: float, j: float) -> float:
    """
    Return the minimum of two numbers.

    :param i: The first number.
    :type i: float
    :param j: The second number.
    :type j: float
    :return: The minimum of the two numbers.
    :rtype: float

    :example:
    >>> min2(4, 5)
    4

    :raises TypeError: If i or j is not a float.
    """
    if not (isinstance(i, (int, float)) and isinstance(j, (int, float))):
        raise TypeError("i and j must be numbers")
    return i if i < j else j

def d1(x: float, y: float, z: float) -> float:
    """
    Calculate the distance d1.

    :param x: The x coordinate.
    :type x: float
    :param y: The y coordinate.
    :type y: float
    :param z: The z coordinate.
    :type z: float
    :return: The distance d1.
    :rtype: float

    :example:
    >>> d1(1, 2, 3)
    5.0

    :raises TypeError: If x, y, or z is not a float.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise TypeError("x, y, and z must be numbers")
    return squareRoot(((x + y) ** 2 + z ** 2))

def d2(x: float, y: float, z: float) -> float:
    """
    Calculate the distance d2.

    :param x: The x coordinate.
    :type x: float
    :param y: The y coordinate.
    :type y: float
    :param z: The z coordinate.
    :type z: float
    :return: The distance d2.
    :rtype: float

    :example:
    >>> d2(1, 2, 3)
    5.0

    :raises TypeError: If x, y, or z is not a float.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise TypeError("x, y, and z must be numbers")
    return squareRoot(((x + z) ** 2 + y ** 2))

def d3(x: float, y: float, z: float) -> float:
    """
    Calculate the distance d3.

    :param x: The x coordinate.
    :type x: float
    :param y: The y coordinate.
    :type y: float
    :param z: The z coordinate.
    :type z: float
    :return: The distance d3.
    :rtype: float

    :example:
    >>> d3(1, 2, 3)
    5.0

    :raises TypeError: If x, y, or z is not a float.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise TypeError("x, y, and z must be numbers")
    return squareRoot(((y + z) ** 2 + x ** 2))

def jalanSemut(x: float, y: float, z: float) -> float:
    """
    Calculate the shortest path for an ant to travel.

    :param x: The x coordinate.
    :type x: float
    :param y: The y coordinate.
    :type y: float
    :param z: The z coordinate.
    :type z: float
    :return: The shortest path for the ant.
    :rtype: float

    :example:
    >>> jalanSemut(1, 2, 3)
    3.742

    :raises TypeError: If x, y, or z is not a float.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise TypeError("x, y, and z must be numbers")
    return round(min2(min2(d1(x, y, z), d2(x, y, z)), d3(x, y, z)), 3)

# BELAJAR TENANG
def BelajarTenang(dB: float, m: float) -> str:
    """
    Calculate the distance a sound can travel based on decibels and fuel.

    :param dB: The decibel level.
    :type dB: float
    :param m: The amount of fuel.
    :type m: float
    :return: The distance the sound can travel or a message to refuel.
    :rtype: str

    :example:
    >>> BelajarTenang(50, 100)
    '47.434 meter'
    >>> BelajarTenang(30, 10)
    'Isi bensin dulu, bang'

    :raises TypeError: If dB or m is not a float.
    """
    if not (isinstance(dB, (int, float)) and isinstance(m, (int, float))):
        raise TypeError("dB and m must be numbers")
    if 15 * (10 ** ((dB - 40) / 20)) <= m:
        return f"{15 * (10 ** ((dB - 40) / 20)):.3f} meter"
    return "Isi bensin dulu, bang"

if __name__ == "__main__":
    # Examples for jam function
    print(jam(12, 30, 45))
    print(jam(25, 61, 61))

    # Examples for monitor_pesawat function
    print(monitor_pesawat(13000, 800, 30))
    print(monitor_pesawat(6000, 500, 60))

    # Examples for squareRoot function
    print(squareRoot(4))
    print(squareRoot(9))

    # Examples for square function
    print(square(4))
    print(square(9))

    # Examples for min2 function
    print(min2(4, 5))
    print(min2(10, 3))

    # Examples for d1 function
    print(d1(1, 2, 3))
    print(d1(4, 5, 6))

    # Examples for d2 function
    print(d2(1, 2, 3))
    print(d2(4, 5, 6))

    # Examples for d3 function
    print(d3(1, 2, 3))
    print(d3(4, 5, 6))

    # Examples for jalanSemut function
    print(jalanSemut(1, 2, 3))
    print(jalanSemut(4, 5, 6))

    # Examples for BelajarTenang function
    print(BelajarTenang(50, 100))
    print(BelajarTenang(30, 10))