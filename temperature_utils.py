from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius_temp = (fahrenheit_temp - 32) * 5.0/9.0
    return round(celsius_temp, 2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    #pass  # remove pass statement and implement me
    farenhite_temp = (celsius_temp * 9.0/5.0) + 32.0
    return int(farenhite_temp)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    #pass  # remove pass statement and implement me

    result = [] # a list to store the tuples
    for temperature in temperatures:  # for loop that iterates thru each element in temperatures iterable
        if input_unit_of_measurement == "f":
            celsius = (temperature - 32) * 5.0 / 9.0
            result.append((temperature , round(celsius, 2)))
        elif input_unit_of_measurement == "c":
            fahrenheit = (temperature * 9.0 / 5.0) + 32.0
            result.append((temperature, round(fahrenheit, 2)))

    return tuple(result)  #convert the list to tuple