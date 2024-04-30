class Car:
    def __init__(self, make, model):
        self.__make = make  
        self.__model = model
        self.__fuel_level = 100  
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_fuel_level(self):
        return self.__fuel_level
    def drive(self):
        if self.__fuel_level > 0:
            print("Car is driving.")
            self.__fuel_level -= 10
        else:
            print("Out of fuel. Refuel before driving.")
    def refuel(self):
        self.__fuel_level = 100
        print("Car has been refueled.")
my_car = Car("Toyota", "Camry")
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Fuel Level:", my_car.get_fuel_level())
my_car.drive()
my_car.refuel()