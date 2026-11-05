from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, student_id, password):
        super().__init__(name, age, role, password)
        self.student_id = student_id
    
    def __str__(self):
        return f"{self.name} is {self.age}, has the role {self.role}"