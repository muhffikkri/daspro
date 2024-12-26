## Summary

This repository contains Python scripts for creating and manipulating various data types including dates, points, mixed fractions, and student records.

### TANGGAL.PY

#### Description

Create a date type along with its constructor and selectors.

#### Task

Define a date type and implement functions to create and manipulate dates.

#### Definition and Specification

**Function Name:** `makeTanggal`

- **Parameters:**
  - `x` (int): The day.
  - `y` (int): The month.
  - `z` (int): The year.
- **Returns:** A date as a list `[x, y, z]`.
- **Raises:** `TypeError` if `x`, `y`, or `z` is not an integer.

**Function Name:** `tanggal`

- **Parameters:**
  - `arr` (list): The date.
- **Returns:** The day component of the date.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `bulan`

- **Parameters:**
  - `arr` (list): The date.
- **Returns:** The month component of the date.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `tahun`

- **Parameters:**
  - `arr` (list): The date.
- **Returns:** The year component of the date.
- **Raises:** `TypeError` if `arr` is not a list.

#### Example

```python
>>> makeTanggal(24, 9, 2024)
[24, 9, 2024]
>>> tanggal([24, 9, 2024])
24
>>> bulan([24, 9, 2024])
9
>>> tahun([24, 9, 2024])
2024
```

### POINT.PY

#### Description

Create a point type along with its constructor and selectors.

#### Task

Define a point type and implement functions to create and manipulate points.

#### Definition and Specification

**Function Name:** `makePoint`

- **Parameters:**
  - `a` (float): The abscissa of the point.
  - `b` (float): The ordinate of the point.
- **Returns:** A point as a list `[a, b]`.
- **Raises:** `TypeError` if `a` or `b` is not a float.

**Function Name:** `absis`

- **Parameters:**
  - `P` (list): The point.
- **Returns:** The abscissa of the point.
- **Raises:** `TypeError` if `P` is not a list.

**Function Name:** `ordinat`

- **Parameters:**
  - `P` (list): The point.
- **Returns:** The ordinate of the point.
- **Raises:** `TypeError` if `P` is not a list.

**Function Name:** `distance`

- **Parameters:**
  - `P1` (list): The first point.
  - `P2` (list): The second point.
- **Returns:** The distance between the two points.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

**Function Name:** `midpoint`

- **Parameters:**
  - `P1` (list): The first point.
  - `P2` (list): The second point.
- **Returns:** The midpoint between the two points.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

#### Example

```python
>>> makePoint(3.0, 4.0)
[3.0, 4.0]
>>> absis([3.0, 4.0])
3.0
>>> ordinat([3.0, 4.0])
4.0
>>> distance([0, 0], [3, 4])
5.0
>>> midpoint([0, 0], [4, 4])
[2.0, 2.0]
```

### PECAHAN.PY

#### Description

Create a mixed fraction type along with its constructor and selectors.

#### Task

Define a mixed fraction type and implement functions to create and manipulate mixed fractions.

#### Definition and Specification

**Function Name:** `makePecahan`

- **Parameters:**
  - `bil` (int): The integer part of the fraction.
  - `n` (int): The numerator of the fraction.
  - `d` (int): The denominator of the fraction.
- **Returns:** A mixed fraction as a list `[bil, n, d]`.
- **Raises:** `TypeError` if `bil`, `n`, or `d` is not an integer.

**Function Name:** `pemb`

- **Parameters:**
  - `P` (list): The mixed fraction.
- **Returns:** The integer part of the fraction.
- **Raises:** `TypeError` if `P` is not a list.

**Function Name:** `peny`

- **Parameters:**
  - `P` (list): The mixed fraction.
- **Returns:** The numerator of the fraction.
- **Raises:** `TypeError` if `P` is not a list.

**Function Name:** `AddP`

- **Parameters:**
  - `P1` (list): The first fraction.
  - `P2` (list): The second fraction.
- **Returns:** The sum of `P1` and `P2` as a fraction.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

**Function Name:** `SubP`

- **Parameters:**
  - `P1` (list): The first fraction.
  - `P2` (list): The second fraction.
- **Returns:** The difference of `P1` and `P2` as a fraction.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

**Function Name:** `MulP`

- **Parameters:**
  - `P1` (list): The first fraction.
  - `P2` (list): The second fraction.
- **Returns:** The product of `P1` and `P2` as a fraction.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

**Function Name:** `DivP`

- **Parameters:**
  - `P1` (list): The first fraction.
  - `P2` (list): The second fraction.
- **Returns:** The quotient of `P1` and `P2` as a fraction.
- **Raises:** `TypeError` if `P1` or `P2` is not a list.

#### Example

```python
>>> makePecahan(1, 2, 3)
[1, 2, 3]
>>> pemb([1, 2, 3])
1
>>> peny([1, 2, 3])
2
>>> AddP([1, 2, 3], [1, 3, 4])
[1, 17, 12]
>>> SubP([1, 2, 3], [1, 3, 4])
[1, 1, 12]
>>> MulP([1, 2, 3], [1, 3, 4])
[1, 6, 12]
>>> DivP([1, 2, 3], [1, 3, 4])
[1, 8, 9]
```

### MHS.PY

#### Description

Create MHS1, MHS2, and MHS3 types along with their constructors and selectors.

#### Task

Define MHS1, MHS2, and MHS3 types and implement functions to create and manipulate these types.

#### Definition and Specification

**Function Name:** `make_MHS1`

- **Parameters:**
  - `NIM` (str): The student's identification number.
  - `nama` (str): The student's name.
  - `tanggal_lahir` (str): The student's date of birth.
- **Returns:** An MHS1 type as a list `[NIM, nama, tanggal_lahir]`.
- **Raises:** `TypeError` if `NIM`, `nama`, or `tanggal_lahir` is not a string.

**Function Name:** `select_NIM_MHS1`

- **Parameters:**
  - `arr` (list): The MHS1 type.
- **Returns:** The NIM of the MHS1 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `select_nama_MHS1`

- **Parameters:**
  - `arr` (list): The MHS1 type.
- **Returns:** The name of the MHS1 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `select_tanggal_lahir_MHS1`

- **Parameters:**
  - `arr` (list): The MHS1 type.
- **Returns:** The date of birth of the MHS1 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `make_MHS2`

- **Parameters:**
  - `NIM` (str): The student's identification number.
  - `kode_maktul` (str): The course code.
  - `nilai` (int): The grade.
- **Returns:** An MHS2 type as a list `[NIM, kode_maktul, nilai]`.
- **Raises:** `TypeError` if `NIM` or `kode_maktul` is not a string, or if `nilai` is not an integer.

**Function Name:** `select_NIM_MHS2`

- **Parameters:**
  - `arr` (list): The MHS2 type.
- **Returns:** The NIM of the MHS2 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `select_kode_matkul_MHS2`

- **Parameters:**
  - `arr` (list): The MHS2 type.
- **Returns:** The course code of the MHS2 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `select_nilai_MHS2`

- **Parameters:**
  - `arr` (list): The MHS2 type.
- **Returns:** The grade of the MHS2 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `make_MHS3`

- **Parameters:**
  - `kode_matkul` (str): The course code.
  - `nama_matkul` (str): The course name.
- **Returns:** An MHS3 type as a list `[kode_matkul, nama_matkul]`.
- **Raises:** `TypeError` if `kode_matkul` or `nama_matkul` is not a string.

**Function Name:** `select_kode_matkul_MHS3`

- **Parameters:**
  - `arr` (list): The MHS3 type.
- **Returns:** The course code of the MHS3 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `select_nama_matkul_MHS3`

- **Parameters:**
  - `arr` (list): The MHS3 type.
- **Returns:** The course name of the MHS3 type.
- **Raises:** `TypeError` if `arr` is not a list.

**Function Name:** `hitungRangeNilai`

- **Parameters:**
  - `arr` (list): The MHS2 type.
- **Returns:** A list containing the course code, maximum grade, minimum grade, and the range of grades.
- **Raises:** `TypeError` if `arr` is not a list.

#### Example

```python
>>> make_MHS1("24060124130069", "Muhammad Fikri", "24-09-2000")
["24060124130069", "Muhammad Fikri", "24-09-2000"]
>>> select_NIM_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
"24060124130069"
>>> select_nama_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
"Muhammad Fikri"
>>> select_tanggal_lahir_MHS1(["24060124130069", "Muhammad Fikri", "24-09-2000"])
"24-09-2000"
>>> make_MHS2("24060124130069", "IF123", 90)
["24060124130069", "IF123", 90]
>>> select_NIM_MHS2(["24060124130069", "IF123", 90])
"24060124130069"
>>> select_kode_matkul_MHS2(["24060124130069", "IF123", 90])
"IF123"
>>> select_nilai_MHS2(["24060124130069", "IF123", 90])
90
>>> make_MHS3("IF123", "Data Structures")
["IF123", "Data Structures"]
>>> select_kode_matkul_MHS3(["IF123", "Data Structures"])
"IF123"
>>> select_nama_matkul_MHS3(["IF123", "Data Structures"])
"Data Structures"
>>> hitungRangeNilai(["IF123", [90, 80, 70, 60]])
["IF123", 90, 60, 30]
```
