# Importing dataclass module
from dataclasses import dataclass


@dataclass
class Student:  # A class for holding a student details

    # Attributes Declaration
    name: str
    college_id: int
    gpa: float


def main():
    alice = Student("Alice", 14785, 7.5)
    bob = Student("Bob", 45698, 8.0)
    enola = Student("Enola", 78963, 8.9)

    # Accessing attributes of Student class
    print("Name: {}, College ID: {}, GPA: {}".format(alice.name, alice.college_id, alice.gpa))
    print("Name: {}, College ID: {}, GPA: {}".format(bob.name, bob.college_id, bob.gpa))
    print("Name: {}, College ID: {}, GPA: {}".format(enola.name, enola.college_id, enola.gpa))

    # printing all instances of Student class
    print(alice)
    print(bob)
    print(enola)


if __name__ == '__main__':
    main()