import datetime
from Student import Student
from typing import Dict, List
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
            lines = file.readlines()
            if not lines:
                print("File is empty")
                return dict()
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
                grades_as_numbers = []

                for grade in grades:
                    converted_grade = safe_convert_to_float(grade)
                    if converted_grade is None:
                        if grade == "":
                            print(name + ":", "has empty grade")
                            continue
                        else:
                            print(name + ":", f"Invalid grade: {grade}")
                            continue
                    if converted_grade < Grade.Min or converted_grade > Grade.Max:
                        print(name + ":", f"Invalid grade: {converted_grade}")
                        continue
                    grades_as_numbers.append(converted_grade)

                result[name] = Student(name, grades_as_numbers)
        return result
    except FileNotFoundError:
        print(f"File [{filename}] not found")
        return result


def show_result(students: List[Student]) -> None:
    for student in students:
        student.show_result()
        print('Is passed:', student.is_passed())
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"))


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
