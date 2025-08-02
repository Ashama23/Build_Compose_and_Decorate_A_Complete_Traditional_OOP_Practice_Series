class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        print(f"Employee created: {self.name} (ID: {self.employee_id})")

    def get_info(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # A list to hold references to Employee objects
        print(f"Department created: {self.name}")

    def add_employee(self, employee):
        print(f"Adding {employee.name} to the {self.name} department.")
        self.employees.append(employee)

    def display_employees(self):
        print(f"\n--- Employees in the {self.name} Department ---")
        if not self.employees:
            print("No employees in this department.")
        for employee in self.employees:
            print(f"- {employee.get_info()}")
        print("------------------------------------------")

emp1 = Employee("Alice Johnson", "E101")
emp2 = Employee("Bob Williams", "E102")

print("\n------------------------------------------------\n")

hr_department = Department("Human Resources")

hr_department.add_employee(emp1)
hr_department.add_employee(emp2)
hr_department.display_employees()

print("\n------------------------------------------------\n")
print("Deleting the Human Resources department.")
del hr_department

print("\n------------------------------------------------\n")
print("Checking if the original Employee objects still exist after deleting the department:")
print(f"Object emp1 still exists: {emp1.get_info()}")
print(f"Object emp2 still exists: {emp2.get_info()}")