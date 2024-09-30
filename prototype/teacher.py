import copy
from person import Person

# concrete prototype 1


class Teacher(Person):
    def __init__(self, name: str, course: str) -> None:
        super().__init__(name)
        self._course = course

    def clone(self):
        return copy.copy(self)

    def display(self):
        print("teacher was cloned")
        print(f"name> {self._name} teaches {self._course}")

    def get_course(self):
        return self._course

    def set_course(self, course: str):
        self._course = course
