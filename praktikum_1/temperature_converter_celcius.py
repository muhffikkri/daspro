def temperature_converter_celcius(temperature: int, scale: str) -> float:
    """
    Convert temperature from Celsius to the specified scale.

    :param temperature: The temperature in Celsius.
    :type temperature: int
    :param scale: The scale to convert to. Can be 'r' (Reamur), 'f' (Fahrenheit), or 'k' (Kelvin).
    :type scale: str
    :return: The converted temperature.
    :rtype: float

    :example:
    >>> temperature_converter_celcius(50, "r")
    40.0
    >>> temperature_converter_celcius(50, "f")
    122.0
    >>> temperature_converter_celcius(50, "k")
    323.0
    """
    match scale:
        case "r" | "reamur":
            return temperature * 4 / 5
        case "f" | "fahrenheit":
            return temperature * 9 / 5 + 32
        case "k" | "kelvin":
            return temperature + 273
        case _:
            raise ValueError("Invalid scale: must be 'r', 'f', or 'k'")

if __name__ == "__main__":
    print(temperature_converter_celcius(50, "r"))  # Output: 40.0
    print(temperature_converter_celcius(50, "f"))  # Output: 122.0
    print(temperature_converter_celcius(50, "k"))  # Output: 323.0