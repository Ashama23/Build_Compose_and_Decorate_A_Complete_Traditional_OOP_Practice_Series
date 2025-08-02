class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
        print(f"Engine with {horsepower}hp ({fuel_type}) created.")

    def start(self):
        if not self.is_running:
            print("Engine is starting... Vroom Vroom!")
            self.is_running = True
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            print("Engine is stopping.")
            self.is_running = False
        else:
            print("Engine is already off.")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: The Car has an Engine
        print(f"A {make} {model} has been built.")

    def start_car(self):
        print(f"Trying to start the {self.make} {self.model}.")
        self.engine.start()

    def stop_car(self):
        print(f"Trying to stop the {self.make} {self.model}.")
        self.engine.stop()

    def get_car_info(self):
        print("\n--- Car Details ---")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Engine Horsepower: {self.engine.horsepower}")
        print(f"Engine Fuel Type: {self.engine.fuel_type}")
        print("--------------------")


my_engine = Engine(300, "Gasoline")
my_car = Car("Ford", "Mustang", my_engine)
my_car.start_car()  
my_car.start_car()  

print("\nDriving around...")

my_car.stop_car()   
my_car.get_car_info()