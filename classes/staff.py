from classes.person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    
    def __str__(self):
        return f"{self.name} is {self.age}, has the role {self.role}"
