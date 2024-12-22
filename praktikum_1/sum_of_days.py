# Tugas Daspro Kelas

# 1 januari sabtu
# Apakah lusa adalah kamis
# print(7 % 7) 0 sabtu
# print(1 % 7) 1 minggu
# print(2 % 7) 2 senin
# print(3 % 7) 3 selasa 
# print(4 % 7) 4 rabu
# print(5 % 7) 5 kamis
# print(6 % 7) 6 jumat

def day_per_month(month: int) :
    if month == 1 : return 1
    elif month == 2 : return 32
    elif month == 3 : return 60 
    elif month == 4 : return 91
    elif month == 5 : return 121
    elif month == 6 : return 152
    elif month == 7 : return 181
    elif month == 8 : return 213
    elif month == 9 : return 244
    elif month == 10 : return 274
    elif month == 11 : return 305
    elif month == 12 : return 335

def sum_of_days(day: int, month: int, year: int) :
    return day_per_month(month) + day - 1 + (1 if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else 0)

# list_of_day = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

def show_day(days: int) : 
    order_of_day = (days % 7) - 1
    if order_of_day == 0 : return "Sabtu"
    elif order_of_day == 1 : return "Minggu"
    elif order_of_day == 2 : return "Senin"
    elif order_of_day == 3 : return "Selasa"
    elif order_of_day == 4 : return "Rabu"
    elif order_of_day == 5 : return "Kamis"
    elif order_of_day == 6 : return "Jumat"
    # return list_of_day[(days % 7) - 1]

# def is_the_day_after_tomorrow_thursday(days: int) :
    # return [show_day(days + 2) == "Kamis", show_day(days - 7)]
    # return show_day(days + 2) == "Kamis"

def is_the_day_after_tomorrow_thursday(day: int, month: int, year: int) :
    return show_day(sum_of_days(day + 2, month, year)) == "Kamis"

# print(show_day(sum_of_days(30,8,2000))) # Rabu
# print(is_the_day_after_tomorrow_thursday(30,8,2000)) # False
# print(show_day(sum_of_days(25,6,2004))) # Minggu
# print(is_the_day_after_tomorrow_thursday(25,6,2004)) # False
# print(show_day(sum_of_days(11,4,2020))) # Selasa
# print(is_the_day_after_tomorrow_thursday(4,1,2020)) # True