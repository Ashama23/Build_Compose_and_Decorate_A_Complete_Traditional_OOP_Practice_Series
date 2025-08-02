class Person:
    def __init__(self, name):
        print(f"Person constructor called for {name}")
        self.name = name

    def display_info(self):
        return f"Name: {self.name}"

class Teacher(Person):
    def __init__(self, name, subject):
        print("Teacher constructor is starting...")
        super().__init__(name)
        self.subject = subject
        print("Teacher constructor finished.")


    def display_info(self):
        person_info = super().display_info()
        return f"{person_info}, Subject: {self.subject}"

teacher = Teacher("Dr. Evelyn Reed", "Physics")

print("\n--- Teacher Information ---")
print(teacher.display_info())
print(f"Direct access to name: {teacher.name}")
print(f"Direct access to subject: {teacher.subject}")