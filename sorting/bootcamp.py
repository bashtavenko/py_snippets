"""Sorting bootcamp."""


class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name


def run():
    students = [
        Student("A", 4.0),
        Student("C", 3.0),
        Student("B", 2.0),
        Student("D", 3.2),
    ]

    # Sorted function (returns new array)
    sorted_by_name = sorted(students)  # uses object __lt__
    # Use lambda
    sorted_by_gpa = sorted(students, key=lambda student: student.gpa)

    # In-place by gpa
    students.sort(key=lambda s: s.gpa, reverse=False)

    # Use get function for simple cases where we have key - value.
    table = {"a": 1, "b": 10, "c": 3}
    sorted_keys = sorted(table, key=table.get)

    # Sort dictionary by key into list of tuples
    table = {"a": 1, "b": 10, "c": 3}
    sorted_by_key = sorted(table.items())
    sorted_by_value = sorted(table.items(), key=lambda x: x[1])


if __name__=="__main__":
    print(run())
