from typing import List


class Student:

    def __init__(self, name: str, grades: List[float]):
        self.name = name
        self.grades = grades

    def calculate_average(self) -> float:
        return sum(self.grades) / len(self.grades)

    def is_passed(self) -> bool:
        return self.calculate_average() >= 2.0 and len(self.grades) >= 3

    def show_result(self):
        print("Name: ", self.name)
        print("Average: ", self.calculate_average())
