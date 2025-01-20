# modify the Car class to 
# encapsulate the brand attribute making it private
# and provide a getter mehtod for it

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
    


my_tesla = ElectricCar("Tesla","Model S","85kwh")
print(my_tesla.full_name())
print(my_tesla.get_brand())
print(my_tesla.__brand)
