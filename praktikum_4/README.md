# Summary

## LATIHANA.PY

### Description

Create recursive functions.

### Task

Implement recursive functions to perform various arithmetic operations.

### Definition and Specification

#### Function Name: `faktorial`

- **Parameters**: `n` (int): The number to calculate the factorial of.
- **Returns**: The factorial of `n`.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `fibonacci`

- **Parameters**: `n` (int): The position in the Fibonacci sequence.
- **Returns**: The nth Fibonacci number.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `tambah`

- **Parameters**: `x` (int): The first number.
- **y** (int): The second number.
- **Returns**: The sum of `x` and `y`.
- **Raises**: `TypeError` if `x` or `y` is not an integer.

#### Function Name: `kurang`

- **Parameters**: `x` (int): The first number.
- **y** (int): The second number.
- **Returns**: The result of `x` minus `y`.
- **Raises**: `TypeError` if `x` or `y` is not an integer.

#### Function Name: `bagi`

- **Parameters**: `x` (int): The dividend.
- **y** (int): The divisor.
- **Returns**: The quotient of `x` divided by `y`.
- **Raises**: `TypeError` if `x` or `y` is not an integer.

#### Function Name: `pangkat`

- **Parameters**: `x` (int): The base.
- **y** (int): The exponent.
- **Returns**: The result of `x` raised to the power of `y`.
- **Raises**: `TypeError` if `x` or `y` is not an integer.

#### Function Name: `kali`

- **Parameters**: `x` (int): The first number.
- **y** (int): The second number.
- **Returns**: The product of `x` and `y`.
- **Raises**: `TypeError` if `x` or `y` is not an integer.

### Example

```python
>>> faktorial(5)
120
>>> fibonacci(5)
5
>>> tambah(5, 5)
10
>>> kurang(5, 5)
0
>>> bagi(5, 5)
1
>>> pangkat(5, 3)
125
>>> kali(5, 3)
15
```

## LATIHANB.PY

### Description

Create recursive functions.

### Task

Implement recursive functions to calculate various series and sums.

### Definition and Specification

#### Function Name: `multiple_three_series`

- **Parameters**: `n` (int): The term position in the series.
- **Returns**: The nth term of the series.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `real_number_series`

- **Parameters**: `n` (int): The number of terms to sum.
- **Returns**: The sum of the first `n` real numbers.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `sum_of_multiple_three_series`

- **Parameters**: `n` (int): The number of terms to sum.
- **Returns**: The sum of the first `n` terms of the series.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `sum_of_three_power_n_series`

- **Parameters**: `n` (int): The number of terms to sum.
- **Returns**: The sum of the series.
- **Raises**: `TypeError` if `n` is not an integer.

#### Function Name: `sum_of_square_series`

- **Parameters**: `n` (int): The number of terms to sum.
- **Returns**: The sum of the series.
- **Raises**: `TypeError` if `n` is not an integer.

### Example

```python
>>> multiple_three_series(5)
15
>>> real_number_series(5)
15
>>> sum_of_multiple_three_series(3)
18
>>> sum_of_three_power_n_series(3)
13
>>> sum_of_square_series(3)
14
```
