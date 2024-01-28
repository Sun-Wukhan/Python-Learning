class Insurance: 
    def __init__(self, make, model, year, driver, age):
        self.make = make 
        self.model = model 
        self.year = year 
        self.driver = driver 
        self.age = age
        print(make, model, year, driver, age) 
        
    def set_insurance(self):
        print(f"{self.make}, {self.model}, {self.year}, {self.driver}, {self.age}")
        
    

insurance = Insurance("Toyota", "Camry", "2023", "Navid", 30)

insurance.set_insurance()
        
    