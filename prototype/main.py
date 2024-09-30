# client
from student import Student
from teacher import Teacher


def main():
    teacher = Teacher("t A", "course A1")
    teacherClone = teacher.clone()
    teacherClone.display()

    student = Student("s A", teacherClone)
    studentClone = student.clone()
    studentClone.display()

    # modify teacher clone
    teacherClone.set_course("course B1")
    studentClone.display()


if __name__ == "__main__":
    main()
