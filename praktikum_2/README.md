# Praktikum 2

## Summary

This repository contains several Python scripts for different tasks. Below are the descriptions and specifications for each script.

### MEANOLYMPIQUE.PY

#### Description

You are tasked with calculating the mean of four numbers after removing the smallest and largest values. This is known as the "Olympic mean." The function `MO(i, j, k, l, procedure)` will compute this mean using one of two procedures. If `procedure` is 1, it uses separate functions to find the minimum and maximum values. If `procedure` is 2, it uses lambda functions to achieve the same result.

#### Task

Calculate the Olympic mean of four numbers after removing the smallest and largest values.

#### Definition and Specification

- **Function Name:** `MO`
- **Parameters:**
  - `i` (int): The first number.
  - `j` (int): The second number.
  - `k` (int): The third number.
  - `l` (int): The fourth number.
  - `procedure` (int): The procedure to use (1 or 2).
- **Returns:** The Olympic mean of the four numbers.
- **Raises:** `ValueError` if `procedure` is not 1 or 2.

#### Example

```python
>>> MO(3, 5, 4, 2, 1)
3.5
>>> MO(2, 2, 2, 2, 1)
2.0
```

### LEASTSQUARE.PY

#### Description

Xaviera, an adventurer who loves exploring maps and measuring distances between places she discovers, gives you an interesting challenge. She provides two coordinate points on the Cartesian plane, (x1, y1) and (x2, y2), and asks you to calculate the distance between these two points using the Euclidean distance formula.

#### Task

Calculate the Euclidean distance between two points on the Cartesian plane.

#### Definition and Specification

- **Function Name:** `least_square`
- **Parameters:**
  - `x1` (float): The x-coordinate of the first point.
  - `y1` (float): The y-coordinate of the first point.
  - `x2` (float): The x-coordinate of the second point.
  - `y2` (float): The y-coordinate of the second point.
- **Returns:** The Euclidean distance between the two points.
- **Raises:** `TypeError` if any of the coordinates are not floats.

#### Example

```python
>>> least_square(0, 0, 3, 4)
5.0
>>> least_square(1, 2, 4, 6)
5.0
```

### ISVALID.PY

#### Description

Kevin, a meticulous researcher, receives a report about the mysterious value of a newly discovered object. The data is an integer, and Kevin must determine whether the object is safe or potentially dangerous. The function `is_valid(x)` evaluates the safety of the object based on its value.

#### Task

Determine if the given value is safe based on the specified conditions.

#### Definition and Specification

- **Function Name:** `is_valid`
- **Parameters:**
  - `x` (int): The value of the object to be checked.
- **Returns:** `True` if the value is less than 5 or greater than 500, `False` otherwise.
- **Raises:** `TypeError` if `x` is not an integer.

#### Example

```python
>>> is_valid(4)
True
>>> is_valid(10)
False
```

### ISPOSITIVE.PY

#### Description

Maxwell, a number wizard with a special interest in positive numbers, asks you to create a function that can tell if a number is one of his favorites. The function `is_positif(x)` detects if a number is positive or zero.

#### Task

Determine if the given number is positive or zero.

#### Definition and Specification

- **Function Name:** `is_positif`
- **Parameters:**
  - `x` (float): The number to be checked.
- **Returns:** `True` if the number is positive or zero, `False` otherwise.
- **Raises:** `TypeError` if `x` is not a float.

#### Example

```python
>>> is_positif(1)
True
>>> is_positif(-1)
False
```

### ISORIGIN.PY

#### Description

In a magical isekai world, you need to determine if you are at the origin (0,0) on a two-dimensional Cartesian plane. The function `is_origin(x, y)` tells you whether you are standing at the zero point.

#### Task

Determine if the given coordinates (x, y) are at the origin (0, 0).

#### Definition and Specification

- **Function Name:** `is_origin`
- **Parameters:**
  - `x` (float): The x-coordinate.
  - `y` (float): The y-coordinate.
- **Returns:** `True` if the coordinates are at the origin, `False` otherwise.
- **Raises:** `TypeError` if `x` or `y` is not a float.

#### Example

```python
>>> is_origin(0, 0)
True
>>> is_origin(1, 1)
False
```

### ISANA.PY

#### Description

Maxwell has a specific fondness for the letter 'a'. The function `isAnA(c)` ensures whether the given character is 'a'.

#### Task

Determine if the given character is 'a'.

#### Definition and Specification

- **Function Name:** `isAnA`
- **Parameters:**
  - `c` (str): A single character to be checked.
- **Returns:** `True` if the character is 'a', `False` otherwise.
- **Raises:** `TypeError` if `c` is not a string or if its length is not 1.

#### Example

```python
>>> isAnA('a')
True
>>> isAnA('b')
False
```
