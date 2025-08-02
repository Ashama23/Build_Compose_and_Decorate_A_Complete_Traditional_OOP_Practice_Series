class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  
        print(f"Product '{self.name}' created with price: ${self._price:.2f}")

    @property
    def price(self):
        print(f"Getting price for {self.name}...")
        return self._price

    @price.setter
    def price(self, new_price):
        print(f"Setting price for {self.name}...")
        if new_price >= 0:
            self._price = new_price
        else:
            print("Error: Price cannot be negative.")

    @price.deleter
    def price(self):
        print(f"Deleting price for {self.name}...")
        del self._price
        print("Price has been deleted.")

my_product = Product("Laptop", 999.99)

print("\n--------------------------\n")

current_price = my_product.price
print(f"The current price is: ${current_price:.2f}")
print("\n--------------------------\n")
print("Updating the price...")
my_product.price = 1049.99
print(f"The new price is: ${my_product.price:.2f}")
print("\n--- Trying to set an invalid price ---")
my_product.price = -50  
print(f"Price after invalid attempt: ${my_product.price:.2f}") 

print("\n--------------------------\n")

print("Deleting the product's price...")
del my_product.price

print("\n--- Trying to access the price after deletion ---")
try:
    print(my_product.price)
except AttributeError as e:
    print(f"Error: {e}")