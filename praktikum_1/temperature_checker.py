def temperature_checker(temperature: int) -> str :
    """This function check the value of temperature fits in which category of temperature."""
    if temperature > 99 : 
        return "Steam"
    elif temperature > 0 : 
        return "Liquid"
    else : 
        return "Ice/Solid"

if __name__ == "__main__" : 
    print(temperature_checker(150)) # Steam
    print(temperature_checker(100)) # Steam
    print(temperature_checker(10)) # Liquid
    print(temperature_checker(-10)) # Ice/Solid
