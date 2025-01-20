class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        # self.total_car +=1
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Fuel and Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return f"{self.__model} hai"
    
class ElectricCar(Car):
    
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def fuel_type(self):
        return "Electricity"

my_car = Car("Tata","Safari")
my_superCar = Car("LamborLamborghini","Aventador")
my_tesla = ElectricCar("Tesla","Model S","85kwh")


class Battery:
    def battery(self):
        return "this is battery"

class Engine:
    def engine(self):
        return "This is engine"

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar2("Tesla","Model A")

print(my_new_tesla.engine())
print(my_new_tesla.battery())