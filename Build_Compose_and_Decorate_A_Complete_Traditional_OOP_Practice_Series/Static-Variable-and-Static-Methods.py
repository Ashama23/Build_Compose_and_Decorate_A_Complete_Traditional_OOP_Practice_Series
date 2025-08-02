class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b

result = MathUtils.add(5, 3)
result = MathUtils.subtract(10, 4)
print(f"The sum is: {result}")