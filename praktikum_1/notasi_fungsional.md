Judul Nama Fungsi (Parameter Formal)
DEFINISI DAN SPESIFIKASI

Nama-Fungsi : domain -> range
{(Nama-Fungsi) mengembalikan nilai }

DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

REALISASI
Nama-Fungsi (list parameter) : ekspresi

APLIKASI
Nama-Fungsi (list parameter) -> hasil

# Tugas 1 - Tugas Kelas

Apakah Lusa Adalah Hari Kamis, Penanggalan isTheDayAfterTomorrowThursday(days)

DEFINISI DAN SPESIFIKASI

isTheDayAfterTomorrowThursday : int -> boolean
{isTheDayAfterTomorrowThursday(days) Mengembalikan nilai boolean dari proses pengecekan apakah lusa adalah hari kamis}

DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

dayPerMonth : int -> int
{dayPerMonth(month) : menerima input berupa bulan dalam integer dan mengembalikan jumlah hari dari tanggal 1 bulan 1 hingga tanggal 1 bulan (month)}

sumOfDays : int, int, int -> int
{sumOfDays(day, month, year) menjumlahkan hari dari input yang diberikan - 1 dengan jumlah hari dari fungsi dayPerMonth serta menambah 1 jika tahun kabisat}

showDay : int -> str
{showDay(days) menerima input berupa angka dan mengembalikan hari dari perhitungan modula}

REALISASI

```
dayPerMonth(month) :

depend on month
month == 1 : 1
month == 2 : 32
month == 3 : 60
month == 4 : 91
month == 5 : 121
month == 6 : 152
month == 7 : 181
month == 8 : 213
month == 9 : 244
month == 10 : 274
month == 11 : 305
month == 12 : 335

sumOfDays(day, month, year) :
day_per_month(month) + day - 1 + (1 if month > 2 and ((year mod 4 == 0 and not(year mod 100 == 0)) or year mod 400 == 0) else 0)

showDay(day) :
let orderOfDay = (days mod 7) - 1
depend on orderOfDay
orderOfDay == 0 : "Sabtu"
orderOfDay == 1 : "Minggu"
orderOfDay == 2 : "Senin"
orderOfDay == 3 : "Selasa"
orderOfDay == 4 : "Rabu"
orderOfDay == 5 : "Kamis"
orderOfDay == 6 : "Jumat"

isTheDayAfterTomorrowThursday(day, month, year) :
show_day(sum_of_days(day + 2, month, year)) == "Kamis"
```

APLIKASI

```
isTheDayAfterTomorrowThurday(30, 8, 2000) -> (Rabu + 2) False
isTheDayAfterTomorrowThurday(25, 6, 2004) -> (Minggu + 2) False
isTheDayAfterTomorrowThurday(11, 4, 2020) -> (Selasa + 2) True
```

# Tugas 2 - Praktikum

## No 1 - Temperature Converter Celsius

Konverter Temperatur TemperatureConverterCelsius(temperature, scale)

DEFINISI DAN SPESIFIKASI

temperatureConverterCelsius: int, str -> real
{temperatureConverterCelsius(temperature, scale) mengonversi inputan skala celsius ke skala temperatur lain dengan kode string}

REALISASI

```
temperatureConverterCelsius(temperature, scale) :
depend on scale
scale == "r" : temperature x 4/5
scale == "f" : temperature x 9/5 + 32
scale == "k" : temperature + 273
```

APLIKASI

```
temperatureConverterCelsius(50, "r") -> 40.0
temperatureConverterCelsius(50, "f") -> 122.0
temperatureConverterCelsius(50, "k") -> 323
```

## No 2 : Temperature Checker

Temperature Checker temperatureChecker(temperature)

DEFINISI DAN SPESIFIKASI

temperatureChecker: int -> str
{temperatureChecker(temperature) membaca temperatur dan menerjemahkan ke wujud benda nya}

REALISASI

```
temperatureChecker(temperature) :
depend on temperature
temperature >= 100 : "Uap"
0 > temperature > 100 : "Cair"
temperature <=0 : "Es (Padat)"
```

APLIKASI

```
temperatureChecker(150) -> Uap
temperatureChecker(100) -> Uap
temperatureChecker(10) -> Cair
temperatureChecker(-10) -> Es (Padat)
```

## No 3 : Triangle Checker

Triangle Checker triangleChecker(side1, side2, side3)

DEFINISI DAN SPESIFIKASI

triangleChecker: int, int, int -> str
{triangleChecker(side1, side2, side3) mengembalikan tipe segitiga sesuai dengan 3 input}

REALISASI

```
triangleChecker(side1, side2, side3) :
depend on side1, side2, side3
side1 == side2 and side2 == side3 : "Segitiga sama sisi"
side1 == side2 or side2 == side3 or side3 == side1 : "Segitiga sama kaki"
<!-- not(side1 == side2) or not(side2 == side3) or not(side1 == side3) : "Segitiga sembarang" -->
else : "Segitiga sembarang"
```

APLIKASI

```
triangleChecker(1,1,1) -> Segitiga sama sisi
triangleChecker(1,1,2) -> Segitiga sama kaki
triangleChecker(3,2,1) -> Segitiga sembarang
```

## NO 4 : Division Between 2 Square Roots

Division Between 2 Square Roots divisonBetween2SquareRoots(a, b, c)

DEFINISI DAN SPESIFIKASI

divisionBetween2SquareRoots : int, int, int -> literal(real, str)
{divisionBetween2SquareRoots(a, b, c) mengembalikan pembagian dari akar yang lebih besar dibagi akar yang lebih kecil}

DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

square: int -> int
{square(s) mengembalikan nilai kuadrat dari (s)}

discriminant: int, int, int, -> int
{discriminant(a, b, c) mengembalikan nilai diskriminan dari input}

roots1: int, int, int -> real
{roots1(a, b, c) mengembalikan nilai dari salah satu akar rumus abc}

roots2: int, int, int -> real
{roots2(a, b, c) mengembalikan nilai dari salah satu akar rumus abc}

REALISASI

```
square(s) : s x s

discriminant(a, b, c) : square(b) - 4 x a x c

roots1(a, b, c) : (-b + discriminant(a, b, c)) / 2 x a

roots2(a, b, c) : (-b - discriminant(a, b, c)) / 2 x a

divisionBetween2SquareRoots(a, b, c) :
if discriminant(a, b, c) < 0 : "The given value return complex number"
else :
(roots_2(a, b, c) / roots_1(a, b, c) if roots_2(a, b, c) > roots_1(a, b, c) else roots_1(a, b, c) / roots_2(a, b, c))
```

APLIKASI

```
division_between_2_square_roots(1,1,1) -> The given value return complex number
division_between_2_square_roots(1,-5,6) -> 1.5
division_between_2_square_roots(1,5,6) -> 0.666666666666
division_between_2_square_roots(1,-4,4) -> 1.0
```
