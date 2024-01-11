class InvalidModelException(Exception):
    def __init__(self, model, message="Model is not Valid"):
        self.model = model
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.model} -> {self.message}"

class Car: 
    valid_models = ["Corolla", "Civic", "Camry", "Accord"]
    
    def __init__(self, make, model, year):  # Add 'year' here
        if model not in Car.valid_models:
            raise InvalidModelException(model)
        self.make = make 
        self.model = model 
        self.year = year  # Set 'year' as an attribute

# Now create Car instances
try:
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Mustang", 2019)  # This should raise an exception
except InvalidModelException as e:
    print(f"Error: {e}")
