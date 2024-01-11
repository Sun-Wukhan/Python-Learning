class Car: 
    def __init__(self, make, model, year, cost=None, insuree=None):
        self.make = make 
        self.model = model 
        self.year = year 
        self.cost = cost 
        self.insuree = insuree
        
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")
        if self.cost and self.insuree: 
            print(f"Insurance Cost: {self.cost}, Insuree: {self.insuree}")
    
    def set_insurance_info(self, cost, insuree): 
        self.cost = cost 
        self.insuree = insuree
        print(f"insurance Info set")


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Lexus", "RC350", 2022, 100, "Adina")
car1.set_insurance_info(100, "Navid")
car1.display_info()