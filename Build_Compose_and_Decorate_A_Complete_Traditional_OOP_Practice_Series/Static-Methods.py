class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
temp_celsius_1 = 0
temp_celsius_2 = 25
temp_celsius_3 = 100

temp_fahrenheit_1 = TemperatureConverter.celsius_to_fahrenheit(temp_celsius_1)
temp_fahrenheit_2 = TemperatureConverter.celsius_to_fahrenheit(temp_celsius_2)
temp_fahrenheit_3 = TemperatureConverter.celsius_to_fahrenheit(temp_celsius_3)

print(f"{temp_celsius_1}°C is equal to {temp_fahrenheit_1}°F")
print(f"{temp_celsius_2}°C is equal to {temp_fahrenheit_2}°F")
print(f"{temp_celsius_3}°C is equal to {temp_fahrenheit_3}°F")