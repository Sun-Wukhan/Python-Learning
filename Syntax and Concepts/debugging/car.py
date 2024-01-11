class InvalidModelException(Exception):
    def __init__(self, model, message="Model is not Valid"):
        self.model = model
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.model} -> {self.message}"

class Car: 
    valid_models = ["Corolla", "Civic", "Camry", "Accord"]
    
    def __init__(self, make, model, year):
        if model not in Car.valid_models:
            raise InvalidModelException(model)
        self.make = make 
        self.model = model 
        self.year = year