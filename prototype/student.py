import copy
from person import Person
from teacher import Teacher

# concrete prototype 2


class Student(Person):
    def __init__(self, name: str, teacher: Teacher) -> None:
        super().__init__(name)
        self._teacher = teacher

    def clone(self):
        # return copy.copy(self)
        return copy.deepcopy(self)

    def display(self):
        print("student was cloned")
        print(
            f"name> {self._name} teaches {self._teacher.get_course()} by teacher {self._teacher.get_name()}"
        )

    def get_course(self):
        return self._course

    def set_course(self, course: str):
        self._course = course
