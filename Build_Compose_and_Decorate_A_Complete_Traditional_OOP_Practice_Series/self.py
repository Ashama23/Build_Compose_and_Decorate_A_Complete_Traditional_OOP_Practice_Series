class Student:

    def __init__(self, name, marks):
        print(f"Creating a new student object for {name}...")
        self.name = name
        self.marks = marks

    def display(self):
        print("--------------------")
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")
        print("--------------------")

if __name__ == "__main__":
    student1 = Student("Alice Smith", 92)
    student2 = Student("Bob Johnson", 85)
    print("\nDisplaying details for the first student:")
    student1.display()
    print("\nDisplaying details for the second student:")
    student2.display()