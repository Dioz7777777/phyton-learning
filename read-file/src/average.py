def main(file_name: str) -> None:
    with open(file_name, "r") as file:
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
            print(name + ":", average)
