def temperature_converter_celcius(temperature: int, scale: str) :
    if scale == "r" or scale == "reamur" :
        return temperature * 4/5
    elif scale == "f" or scale == "fahrenheit" :
        return temperature * 9/5 + 32
    elif scale == "k" or scale == "kelvin" :
        return temperature + 273
    return temperature

print(temperature_converter_celcius(50,"r")) # 40.0
print(temperature_converter_celcius(50,"f")) # 122.0
print(temperature_converter_celcius(50,"k")) # 323