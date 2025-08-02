class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print(f"{self.name}, the {self.breed}, has been created!")

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
neighbors_dog = Dog("Lucy", "Beagle")

print("\n--- Let's hear the dogs bark ---")
my_dog.bark()
neighbors_dog.bark()