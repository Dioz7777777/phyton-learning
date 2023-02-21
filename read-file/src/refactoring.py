import datetime
from typing import Dict, List

from logger import debug
from Student import Student
from Grade import Grade


def safe_convert_to_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def read_grades_from_file(filename: str) -> Dict[str, Student]:
    result = {}
    try:
        with open(filename, "r") as file:
            for line in file.readlines():
                if not line:
                    debug("File is empty")
                    continue
                line_without_spaces = line.replace(" ", "")
                name, *grades = line_without_spaces.split(",")
                grades_as_numbers = []

                for grade in grades:
                    converted_grade = safe_convert_to_float(grade)
                    if converted_grade is None:
                        if grade == "":
                            debug(name + ":" + "has empty grade")
                            continue
                        else:
                            debug(name + ":" + f"Invalid grade: {grade}")
                            continue
                    if converted_grade < Grade.Min or converted_grade > Grade.Max:
                        debug(name + ":" + f"Invalid grade: {converted_grade}")
                        continue
                    grades_as_numbers.append(converted_grade)

                result[name] = Student(name, grades_as_numbers)
        return result
    except FileNotFoundError:
        debug(f"File [{filename}] not found")
        return result


def show_result(students: List[Student]) -> None:
    for student in students:
        student.show_result()
        debug('Is passed:' + str(student.is_passed()))
    now = datetime.datetime.now()
    debug(now.strftime("%Y-%m-%d %H:%M"))


def main(file_name: str, sort_by: str) -> None:
    grades_result = read_grades_from_file(file_name)

    if sort_by == "N":
        sorted_by_name = dict(sorted(grades_result.items()))
        items = list(sorted_by_name.values())
        show_result(items)
    elif sort_by == "A":
        sorted_by_average = dict(sorted(grades_result.items(), key=lambda x: x[1].calculate_average()))
        items = list(sorted_by_average.values())
        show_result(items)
