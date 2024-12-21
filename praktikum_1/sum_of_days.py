def show_day(days: int) -> str:
    """
    Return the day of the week given the number of days since 1 January 1900. 1 January 1900 is a Saturday.

    :param days: The number of days since 1 January 1900.
    :type days: int
    :return: The day of the week.
    :rtype: str

    :example:
    >>> show_day(0)
    'Saturday'
    >>> show_day(1)
    'Sunday'
    """
    match days % 7:
        case 0: return "Saturday"
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"

def is_leap_year(year: int) -> bool:
    """
    Return True if the year is a leap year, False otherwise.

    :param year: The year to check.
    :type year: int
    :return: True if the year is a leap year, False otherwise.
    :rtype: bool

    :example:
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2021)
    False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_per_month(month: int) -> int:
    """
    Return the number of days in the given month.

    This function returns the number of days from day one to day one in the given month. Except for January, the function will return the cumulative number of days
    : Formula : 1 + number of days in the given month 
    : January : 1 + 0 = 1
    : February : 1 + 28 = 32
    : March : 1 + 28 + 31 = 60
    : April : 1 + 31 + 28 + 31 = 91
    : May : 1 + 31 + 28 + 31 + 30 = 121
    : June : 1 + 31 + 28 + 31 + 30 + 31 = 152
    : July : 1 + 31 + 28 + 31 + 30 + 31 + 30 = 181
    : August : 1 + 31 + 28 + 31 + 30 + 31 + 30 + 31 = 213
    : September : 1 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 244
    : October : 1 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 = 274
    : November : 1 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 = 305
    : December : 1 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 = 335
 
    : Example : 
    >>> day_per_month(1)
    1
    >>> day_per_month(2)
    32
    """

    match month : 
        case 1 : return 1
        case 2 : return 32
        case 3 : return 60 
        case 4 : return 91
        case 5 : return 121
        case 6 : return 152
        case 7 : return 181
        case 8 : return 213
        case 9 : return 244
        case 10 : return 274
        case 11 : return 305
        case 12 : return 335

def sum_of_days(day: int, month: int, year: int) -> int :
    """
    Return the sum of days from day one to specific day in the given month and year. 
    If year is a leap year , February will have 29 days. Otherwise, February will have 28 days.
    : Formula : 1 + (day - 1) + sum of days from day one to day one in the given month

    : EXAMPLE : 
    >>> sum_of_days(10, 2, 2024)
    42
    """

    if month > 2 and is_leap_year(year) :
        return day_per_month(month) + day - 1
    else : 
        return day_per_month(month) + day - 1 + 1 


def is_the_day_after_tomorrow_thursday(day: int, month: int, year: int) -> bool :
    """Return true if the day after tomorrow is Thursday, false otherwise"""
    return sum_of_days(day + 2, month, year) % 7 == 5

if __name__ == "__main__" :
    print(sum_of_days(10, 2, 2024)) # Output: 42
    print(is_the_day_after_tomorrow_thursday(10, 2, 2024)) # Output: False
    print(show_day(sum_of_days(10, 2, 2024))) # Output: Saturday

    print(sum_of_days(30, 8, 2000)) # Output: 242
    print(is_the_day_after_tomorrow_thursday(30, 8, 2000)) # Output: False
    print(show_day(sum_of_days(30,8, 2000))) # Output: Wednesday
    
    print(sum_of_days(25, 6, 2024)) # Output: 176
    print(show_day(sum_of_days(25,6,2004))) # Output: Sunday
    print(is_the_day_after_tomorrow_thursday(25,6,2004)) # Output: False