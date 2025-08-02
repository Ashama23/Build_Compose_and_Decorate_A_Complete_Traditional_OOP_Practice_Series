class Car:

    def __init__(self, brand):
        self.brand = brand
        print(f"A new car of brand '{self.brand}' has been created.")

    def start(self):
        print(f"The {self.brand} car is starting... Vroom vroom!")

if __name__ == "__main__":

    my_car = Car("Toyota")

    print("\n--- Accessing public members from outside the class ---")
    car_brand = my_car.brand
    print(f"Accessed public variable 'brand': {car_brand}")
    print("Modifying the public variable 'brand' to 'Honda'...")
    my_car.brand = "Honda"
    print(f"The new brand is: {my_car.brand}")
    print("\nCalling the public method 'start()':")
    my_car.start()

    