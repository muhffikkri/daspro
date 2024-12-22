def is_triangle(side_1: int, side_2: int, side_3: int) :
    return side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2

def triangle_checker(side_1: int, side_2: int, side_3: int) :
    if is_triangle(side_1, side_2, side_3) : 
        if side_1 == side_2 == side_3:
            return "Segitiga sama sisi"
        if side_1 == side_2 or side_2 == side_3 or side_3 == side_1 :
            return "Segitiga sama kaki"

        return "Segitiga sembarang"
    
    return "That's not a triangle"
        

print(triangle_checker(1,1,1)) # Segitiga sama sisi
print(triangle_checker(1,1,2)) # Segitiga sama kaki
print(triangle_checker(3,2,1)) # Segitiga sembarang
print(triangle_checker(15,20,1)) # Segitiga sembarang