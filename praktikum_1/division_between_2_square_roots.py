def square(x: int) : return x*x

def discriminant(a: int, b: int, c: int) :
    return (square(b) - 4*a*c)

def roots_1(a, b, c) : 
    return (-1 * b + (discriminant(a, b, c))**0.5) / 2*a

def roots_2(a, b, c) : 
    return (-1 * b - (discriminant(a, b, c))**0.5) / 2*a

def division_between_2_square_roots(a: int, b: int, c: int) :
    if discriminant(a, b, c) < 0 : return "The given value return complex number"
    # roots_1 = (-1 * b + discriminant(a, b, c)) / 2*a
    # roots_2 = (-1 * b - discriminant(a, b, c)) / 2*a

    # return (roots_2 / roots_1 if roots_2 > roots_1 else roots_1 / roots_2)
    return (roots_2(a, b, c) / roots_1(a, b, c) if roots_2(a, b, c) > roots_1(a, b, c) else roots_1(a, b, c) / roots_2(a, b, c))

print(division_between_2_square_roots(1,1,1)) # The given value return complex number
print(division_between_2_square_roots(1,-5,6)) # 1.5 
print(division_between_2_square_roots(1,-1,-2)) # 1.0
