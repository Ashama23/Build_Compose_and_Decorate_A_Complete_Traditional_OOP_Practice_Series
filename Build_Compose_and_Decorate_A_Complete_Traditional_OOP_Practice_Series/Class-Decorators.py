def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    setattr(cls, 'greet', greet)

    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return f"My name is {self.name}."

person = Person("Alice")
print(f"Original method call: {person.say_name()}")
print(f"Decorated method call: {person.greet()}")
has_greet_method = hasattr(Person, 'greet')
print(f"\nDoes the Person class have a 'greet' method? {has_greet_method}")