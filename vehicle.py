class vehicle:
    def __init__(self,fuel,brand,category,color,year_model,mileage):
        self.fuel = fuel
        self.brand = brand
        self.category = category
        self.color = color
        self.year_model = year_model
        self.mileage = mileage
        
    def return_info(self):
        return f'Brand: {self.brand}, Category: {self.category}, Color: {self.color}, Year Model: {self.year_model}'
        
class car(vehicle):
    pass

class motorbike:
    def __init__(self, fuel, mileage, hours)
        self.hours = hours
        super().__init__(fuel, mileage)
    
    def return_info(self):
        return super().return_info() + f', Hours: {self.hours}'
    
BMW_RT = motorbike('petrol', 5000, 25)
Yaris = car('petrol', 250000)
garage = [BMW_RT, Yaris]
for vehicle in garage:
    print(vehicle.return_info())