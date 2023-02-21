from typing import List
from logger import debug


class Student:

    def __init__(self, name: str, grades: List[float]):
        self.name = name
        self.grades = grades

    def calculate_average(self) -> float:
        try:
            return sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            return 0.0

    def is_passed(self) -> bool:
        return self.calculate_average() >= 2.0 and len(self.grades) >= 3

    def show_result(self):
        debug("Name: " + self.name)
        debug("Average: " + str(self.calculate_average()))
