def temperature_checker(temperature: int) :
    if temperature > 99 : return "Uap"
    elif temperature > 0 : return "Cair"
    return "Es (Padat)"

# print(temperature_checker(150)) # Uap
# print(temperature_checker(100)) # Uap
# print(temperature_checker(10)) # Cair
# print(temperature_checker(-10)) # Es (Padat)
