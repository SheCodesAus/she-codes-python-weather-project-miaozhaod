from audioop import avg
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
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%A %d %B %Y")
    return date
    # done


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
    # list = []
    # with open(weather_data) as csv_file:
    #     reader = csv.reader(csv_file)
    #     for line in reader:
    #         if line != []:
    #             list.append(line)
    # list.pop(0)
    # listResult = []
    # for li in list:
    #     num = [li[0], (int(li[1])), (int(li[2]))]
    #     listResult.append(num)

    weathers = []
    for li in weather_data:
        date = datetime.strptime(li[0], "%Y-%m-%dT%H:%M:%S%z").strftime("%A %d %B %Y")
        low = round((float(li[1]) - 32) * 5 / 9, 1)
        high = round((float(li[2]) - 32) * 5 / 9, 1)
        newLi = [date, low, high]
        weathers.append(newLi)
    # print("weathers: ", weathers) # got a list of weathers[] in the format of date, low, high
    days = len(weathers);
    
    low_temps = []
    for weather in weathers:
        low_temps.append(weather[1])
    # print("low_temps: ", low_temps) # got a list of the low_temps[] in the above weathers[]
    avg_low = round(sum(low_temps) / len(low_temps), 1)
    # print("avg_low: ", avg_low)

    min_low = float(low_temps[0])
    min_low_location = 0
    index = 0
    for low_temp in low_temps:
        if float(low_temp) <= min_low:
            min_low = float(low_temp)
            min_low_location = index
            index += 1
    date_of_min_low = weathers[min_low_location][0]
    # print("min_low | min_low_location | date_of_min_low: ", min_low, "|", min_low_location, "|", date_of_min_low)

    high_temps = []
    for weather in weathers:
        high_temps.append(weather[2])
    # print("high_temps: ", high_temps)  # got a list of the low_temps[] in the above weathers[]
    avg_high = round(sum(high_temps) / len(high_temps), 1)
    # print("avg_high: ", avg_high)

    max_high = float(high_temps[0])
    max_high_location = 0
    index = 0
    for high_temp in high_temps:
        if float(high_temp) >= max_high:
            max_high = float(high_temp)
            max_high_location = index
            index += 1
    date_of_max_high = weathers[max_high_location][0]
    # print("max_high | max_high_location | date_of_max_high: ", max_high, "|", max_high_location, "|", date_of_max_high)

    summary_heading = f"{days} Day Overview"
    lowest_summary = f"The lowest temperature will be {min_low}°C, and will occur on {date_of_min_low}."
    highest_summary = f"The highest temperature will be {max_high}°C, and will occur on {date_of_max_high}."
    avg_low_summary = f"The average low this week is {avg_low}°C."
    avg_high_summary = f"The average high this week is {avg_high}°C."
    summary_result = f"{summary_heading}\n  {lowest_summary}\n  {highest_summary}\n  {avg_low_summary}\n  {avg_high_summary}\n"
    return summary_result

# print(generate_summary("./tests/data/example_one.csv"))


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
