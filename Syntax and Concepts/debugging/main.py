from car import Car, InvalidModelException

try:
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Mustang", 2019)  # This should raise an exception
except InvalidModelException as e:
    print(f"Error: {e}")
