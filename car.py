class car:
    def __init__(self,year,model,make,mileage):
        self.year = year
        self.model = model
        self.make = make
        self.mileage = mileage

    def display_info(self):
        return(self.year, self.make, self.model, self.mileage)

input_name = input("What have you named your car?: ")
input_year = input("What year was your car made?: ")
input_model = input("What car model do you own?: ")
input_mileage = input("What does yout odometer read currently")
        
leonard = car(2007, 'Corolla', 'Toyota', '12400 Miles')

print(leonard.display_info())