# File Name: mahasiswa.py
# Description: Create MHS1, MHS2, and MHS3 types along with their constructors and selectors
# Author: Muhammad Fikri-24060124130069
# Date: September 24, 2024

def make_MHS1(NIM, nama, tanggal_lahir):
    """
    Create an MHS1 type from three elements.

    :param NIM: The student's identification number.
    :type NIM: str
    :param nama: The student's name.
    :type nama: str
    :param tanggal_lahir: The student's date of birth.
    :type tanggal_lahir: str
    :return: An MHS1 type as a list [NIM, nama, tanggal_lahir].
    :rtype: list

    :example:
    >>> make_MHS1("24060124130069", "Muhammad Fikri", "24-09-2000")
    ["24060124130069", "Muhammad Fikri", "24-09-2000"]

    :raises TypeError: If NIM, nama, or tanggal_lahir is not a string.
    """
    if not all(isinstance(i, str) for i in [NIM, nama, tanggal_lahir]):
        raise TypeError("NIM, nama, and tanggal_lahir must be strings")
    return [NIM, nama, tanggal_lahir]

def select_NIM_MHS1(arr):
    """
    Return the NIM of the MHS1 type.

    :param arr: The MHS1 type.
    :type arr: list
    :return: The NIM of the MHS1 type.
    :rtype: str

    :example:
    >>> select_NIM_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
    "24060124130069"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[0]

def select_nama_MHS1(arr):
    """
    Return the name of the MHS1 type.

    :param arr: The MHS1 type.
    :type arr: list
    :return: The name of the MHS1 type.
    :rtype: str

    :example:
    >>> select_nama_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
    "Muhammad Fikri"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[1]

def select_tanggal_lahir_MHS1(arr):
    """
    Return the date of birth of the MHS1 type.

    :param arr: The MHS1 type.
    :type arr: list
    :return: The date of birth of the MHS1 type.
    :rtype: str

    :example:
    >>> select_tanggal_lahir_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
    "24-09-2000"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[2]

def make_MHS2(NIM, kode_maktul, nilai):
    """
    Create an MHS2 type from three elements.

    :param NIM: The student's identification number.
    :type NIM: str
    :param kode_maktul: The course code.
    :type kode_maktul: str
    :param nilai: The grade.
    :type nilai: int
    :return: An MHS2 type as a list [NIM, kode_maktul, nilai].
    :rtype: list

    :example:
    >>> make_MHS2("24060124130069", "IF123", 90)
    ["24060124130069", "IF123", 90]

    :raises TypeError: If NIM or kode_maktul is not a string, or if nilai is not an integer.
    """
    if not (isinstance(NIM, str) and isinstance(kode_maktul, str) and isinstance(nilai, int)):
        raise TypeError("NIM and kode_maktul must be strings, and nilai must be an integer")
    return [NIM, kode_maktul, nilai]

def select_NIM_MHS2(arr):
    """
    Return the NIM of the MHS2 type.

    :param arr: The MHS2 type.
    :type arr: list
    :return: The NIM of the MHS2 type.
    :rtype: str

    :example:
    >>> select_NIM_MHS2(["24060124130069", "IF123", 90])
    "24060124130069"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[0]

def select_kode_matkul_MHS2(arr):
    """
    Return the course code of the MHS2 type.

    :param arr: The MHS2 type.
    :type arr: list
    :return: The course code of the MHS2 type.
    :rtype: str

    :example:
    >>> select_kode_matkul_MHS2(["24060124130069", "IF123", 90])
    "IF123"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[1]

def select_nilai_MHS2(arr):
    """
    Return the grade of the MHS2 type.

    :param arr: The MHS2 type.
    :type arr: list
    :return: The grade of the MHS2 type.
    :rtype: int

    :example:
    >>> select_nilai_MHS2(["24060124130069", "IF123", 90])
    90

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[2]

def make_MHS3(kode_matkul, nama_matkul):
    """
    Create an MHS3 type from two elements.

    :param kode_matkul: The course code.
    :type kode_matkul: str
    :param nama_matkul: The course name.
    :type nama_matkul: str
    :return: An MHS3 type as a list [kode_matkul, nama_matkul].
    :rtype: list

    :example:
    >>> make_MHS3("IF123", "Data Structures")
    ["IF123", "Data Structures"]

    :raises TypeError: If kode_matkul or nama_matkul is not a string.
    """
    if not (isinstance(kode_matkul, str) and isinstance(nama_matkul, str)):
        raise TypeError("kode_matkul and nama_matkul must be strings")
    return [kode_matkul, nama_matkul]

def select_kode_matkul_MHS3(arr):
    """
    Return the course code of the MHS3 type.

    :param arr: The MHS3 type.
    :type arr: list
    :return: The course code of the MHS3 type.
    :rtype: str

    :example:
    >>> select_kode_matkul_MHS3(["IF123", "Data Structures"])
    "IF123"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[0]

def select_nama_matkul_MHS3(arr):
    """
    Return the course name of the MHS3 type.

    :param arr: The MHS3 type.
    :type arr: list
    :return: The course name of the MHS3 type.
    :rtype: str

    :example:
    >>> select_nama_matkul_MHS3(["IF123", "Data Structures"])
    "Data Structures"

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return arr[1]

def hitungRangeNilai(arr):
    """
    Calculate the range of grades for a course.

    :param arr: The MHS2 type.
    :type arr: list
    :return: A list containing the course code, maximum grade, minimum grade, and the range of grades.
    :rtype: list

    :example:
    >>> hitungRangeNilai(["IF123", [90, 80, 70, 60]])
    ["IF123", 90, 60, 30]

    :raises TypeError: If arr is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    return [
        select_kode_matkul_MHS2(arr),
        max(select_nilai_MHS2(arr)),
        min(select_nilai_MHS2(arr)),
        max(select_nilai_MHS2(arr)) - min(select_nilai_MHS2(arr))
    ]

if __name__ == "__main__":
    # Examples that will only run when this file is executed directly
    print(make_MHS1("24060124130069", "Muhammad Fikri", "24-09-2000"))  # Output: ["24060124130069", "Muhammad Fikri", "24-09-2000"]
    print(select_NIM_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"]))  # Output: "24060124130069"
    print(select_nama_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"]))  # Output: "Muhammad Fikri"
    print(select_tanggal_lahir_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"]))  # Output: "24-09-2000"

    print(make_MHS2("24060124130069", "IF123", 90))  # Output: ["24060124130069", "IF123", 90]
    print(select_NIM_MHS2(["24060124130069", "IF123", 90]))  # Output: "24060124130069"
    print(select_kode_matkul_MHS2(["24060124130069", "IF123", 90]))  # Output: "IF123"
    print(select_nilai_MHS2(["24060124130069", "IF123", 90]))  # Output: 90

    print(make_MHS3("IF123", "Data Structures"))  # Output: ["IF123", "Data Structures"]
    print(select_kode_matkul_MHS3(["IF123", "Data Structures"]))  # Output: "IF123"
    print(select_nama_matkul_MHS3(["IF123", "Data Structures"]))  # Output: "Data Structures"

    print(hitungRangeNilai(["IF123", [90, 80, 70, 60]]))  # Output: ["IF123", 90, 60, 30]