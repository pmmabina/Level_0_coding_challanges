def temperature_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32 
    return fahrenheit
print(temperature_to_fahrenheit(0))

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(fahrenheit_celsius(10))
