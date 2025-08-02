class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        print(f"Multiplier object created with a factor of {self.factor}")

    def __call__(self, number):
        print(f"__call__ invoked: Multiplying {number} by {self.factor}")
        return number * self.factor
    
double = Multiplier(2)
triple = Multiplier(3)

print("\n--- Testing if the objects are callable ---")
print(f"Is the 'double' object callable? {callable(double)}")
print(f"Is the 'triple' object callable? {callable(triple)}")
print(f"Is the number 5 callable? {callable(5)}")

print("\n--- Calling the objects like functions ---")
result_double = double(10)  
print(f"Result of double(10): {result_double}")

print("-" * 20)
result_triple = triple(7)
print(f"Result of triple(7): {result_triple}")