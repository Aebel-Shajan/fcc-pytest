import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# Fixtures
@pytest.fixture
def snape():
    return Teacher(name="Severus Snape")

@pytest.fixture
def students():
    return [Student(name="Harry Potter"), Student(name="Hermione Granger"), Student(name="Ron Weasley")]

@pytest.fixture
def classroom(snape, students):
    return Classroom(teacher=snape, students=students, course_title="Potions")

# Parametrized Test for Adding Students
@pytest.mark.parametrize("new_student_name", ["Neville Longbottom", "Draco Malfoy", "Luna Lovegood"])
def test_add_student_success(classroom, new_student_name):
    new_student = Student(name=new_student_name)
    classroom.add_student(new_student)
    assert new_student in classroom.students

# Test adding a student when the class is full
def test_add_student_too_many_students(classroom):
    additional_students = [Student(name=f"Student {i}") for i in range(8)]
    for student in additional_students:
        classroom.add_student(student)
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student(name="Albus Dumbledore"))

# Test removing a student
def test_remove_student(classroom):
    classroom.remove_student("Harry Potter")
    assert all(student.name != "Harry Potter" for student in classroom.students)

# Test changing the teacher
def test_change_teacher(classroom):
    new_teacher = Teacher(name="Albus Dumbledore")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Albus Dumbledore"

# Marking a test as slow
@pytest.mark.slow
def test_add_multiple_students(classroom):
    additional_students = [Student(name=f"Student {i}") for i in range(7)]
    for student in additional_students:
        classroom.add_student(student)
    assert len(classroom.students) == 10
