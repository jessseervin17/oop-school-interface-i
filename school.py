class School:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.students = []

class Person:
    def __init__(self, name, age, role, password):
        self.name=name
        self.age=age
        self.role=role
        self.password=password

class Student(Person):
    def __init__(self, name, age, role, student_id, password):
        super().__init__(name, age, role, password)
        self.student_id = student_id
    
    def __str__(self):
        return f"{self.name} is {self.age}, has the role {self.role}"

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    
    def __str__(self):
        return f"{self.name} is {self.age}, has the role {self.role}"
