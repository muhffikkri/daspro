## Praktikum 1

###

### `division_between_2_square_roots.py`

- **square(x: int) -> int**

  - Returns the square of the given number `x`.

- **square_root(x: int) -> float**

  - Returns the square root of the given number `x`.

- **discriminant(a: int, b: int, c: int) -> float**

  - Returns the discriminant of the quadratic equation `ax^2 + bx + c = 0`.

- **roots(a: int, b: int, c: int, func: Callable[[int, float], float]) -> float**

  - Returns one of the roots of the quadratic equation using the provided function.

- **roots_1(a: int, b: int, c: int) -> float**

  - Returns one of the roots of the quadratic equation `ax^2 + bx + c = 0`.

- **roots_2(a: int, b: int, c: int) -> float**

  - Returns one of the roots of the quadratic equation `ax^2 + bx + c = 0`.

- **division_between_2_square_roots(a: int, b: int, c: int, procedure: int) -> float**
  - Returns 0 if the discriminant is negative, otherwise returns the division between the two roots of the quadratic equation. The greater root divides the smaller one.

### `temperature_converter_celcius.py`

- **temperature_converter_celcius(temperature: int, scale: str) -> float**
  - Converts temperature from Celsius to the specified scale ('r' for Reamur, 'f' for Fahrenheit, 'k' for Kelvin).

### `triangle_checker.py`

- **is_triangle(side_1: int, side_2: int, side_3: int) -> bool**

  - Returns True if the sides form a triangle, False otherwise. A triangle is valid if the sum of any two sides is greater than the third side.

- **triangle_checker(side_1: int, side_2: int, side_3: int) -> str**
  - Returns the type of triangle based on the lengths of its sides. If the sides do not form a triangle, returns 'Not a triangle'. Otherwise, it returns 'Equilateral', 'Isosceles', or 'Scalene' based on the side lengths.

### `sum_of_days.py`

- **show_day(days: int) -> str**

  - Returns the day of the week given the number of days since 1 January 1900. 1 January 1900 is a Saturday.

- **is_leap_year(year: int) -> bool**

  - Returns True if the year is a leap year, False otherwise.

- **day_per_month(month: int) -> int**

  - Returns the number of days in the given month. The function returns the cumulative number of days from the start of the year to the start of the given month.

- **sum_of_days(day: int, month: int, year: int) -> int**

  - Returns the sum of days from day one to a specific day in the given month and year. If the year is a leap year, February will have 29 days; otherwise, February will have 28 days.

- **is_the_day_after_tomorrow_thursday(day: int, month: int, year: int) -> bool**
  - Returns True if the day after tomorrow is Thursday, False otherwise.

### `temperature_checker.py`

- **temperature_checker(temperature: int) -> str**
  - Checks the value of the temperature and categorizes it as 'Steam', 'Liquid', or 'Ice/Solid' based on the temperature value.

Will be updated as soon as the docstring are completed.
