import datetime
from typing import Dict


def read_grades_from_file(filename: str) -> Dict[str, float]:
    result = {}
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line_without_spaces = line.replace(" ", "")
            line_values = line_without_spaces.split(",")
            if not any(line_values):
                print("Empty line")
                continue
            if len(line_values) == 1:
                print(name + ":", "has no grades")
                continue
            name = line_values[0]
            grades = line_values[1:]
            grades_as_numbers = [float(grade) for grade in grades]
            average = sum(grades_as_numbers) / len(grades_as_numbers)
            result[name] = average
    return result


def safe_float_conversion(input_value: str) -> float | None:
    try:
        return float(input_value)
    except ValueError:
        return None


def show_result(dictionary: Dict[str, float]) -> None:
    for key in dictionary.keys():
        value = dictionary[key]
        print(key + ":", value)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"))


def main(file_name: str, sort_by: str) -> None:
    grades_result = read_grades_from_file(file_name)
    if grades_result is None:
        print("File not found")
        return

    if sort_by == "N":
        sorted_by_name = dict(sorted(grades_result.items()))
        show_result(sorted_by_name)
    elif sort_by == "A":
        sorted_by_average = dict(sorted(grades_result.items(), key=lambda x: x[1]))
        show_result(sorted_by_average)
