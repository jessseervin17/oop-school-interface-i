from classes.school import School
from classes.person import Person
from classes.staff import Staff
from classes.student import Student

def test_school_class():
    ridgemont_high = School("Ridgemont")
    assert ridgemont_high.name == "Ridgemont"
    assert ridgemont_high.staff == []
    assert ridgemont_high.students == []

def test_person_class():
    person_info = {"name":"James", "age":23, "role":"Janitor", "password":"password"}
    James = Person(**person_info)
    assert James.name == "James"
    assert James.age == 23
    assert James.role == "Janitor"
    assert James.password == "password"

def test_student_and_staff_classes():
    student_info={"name":"June", "age":14, "role":"Student", "student_id":12345, "password":"ghost"}
    staff_info={"name":"Bruce", "age":49, "role":"Principal", "employee_id":2468, "password":"HotStuff23"}
    June = Student(**student_info)
    Old = Staff(**staff_info)
    assert June.name=="June"
    assert June.student_id == 12345
    assert Old.age==49
    assert Old.role=="Principal"