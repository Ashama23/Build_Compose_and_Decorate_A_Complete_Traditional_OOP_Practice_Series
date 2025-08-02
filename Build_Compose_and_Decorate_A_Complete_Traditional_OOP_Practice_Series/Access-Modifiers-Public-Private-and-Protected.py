class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          
        self._salary = salary     
        self.__ssn = ssn          

    def display_employee_info(self):
        print("--- Displaying Information from within the class ---")
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
    
emp = Employee("John Doe", 80000, "123-45-678")

print("--- Accessing variables directly from the object ---")

try:
    print(f"Public name: {emp.name}")
except AttributeError as e:
    print(e)

try:
    print(f"Protected salary: {emp._salary}")
except AttributeError as e:
    print(e)

try:
    print(f"Private SSN: {emp.__ssn}")
except AttributeError as e:
    print(f"Error accessing private __ssn: {e}")

print("\n")
emp.display_employee_info()
print(f"\nAccessing private SSN with name mangling: {emp._Employee__ssn}")