import csv
from datetime import datetime

DEGREE_SYBMOL = "\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # strptime
    # strftime
    date_object = datetime.strptime(iso_string, "%d %B, %Y")
    return date_object


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = round((float(temp_in_farenheit) - 32) * 5 / 9, 1)
    return temp_in_celcius
    # done


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    for index in range(0, len(weather_data)):
        sum = sum + float(weather_data[index])
    mean = sum / len(weather_data)
    return mean
    # done


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list = []
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if line != []:
                list.append(line)
    list.pop(0)
    listResult = []
    for li in list:
        num = [li[0], (int(li[1])), (int(li[2]))]
        listResult.append(num)
    return listResult
    # done


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        min_value = float(weather_data[0])
        min_location = 0
        index = 0

        for weather in weather_data:
            if float(weather) <= min_value:
                min_value = float(weather)
                min_location = index
            index += 1
        return min_value, min_location
    # done


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        max_value = float(weather_data[0])
        max_location = 0
        index = 0

        for weather in weather_data:
            if float(weather) >= max_value:
                max_value = float(weather)
                max_location = index
            index += 1
        return max_value, max_location
    # done


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    for weather in weather_data:
        return weather


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
