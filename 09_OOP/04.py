#Incapsulation
#Inheritance
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def display_info(self):
        print(f"Car Brand: {self.__brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Full Name: {self.full_name()}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


my_tesla = ElectricCar("Tesla", "Model S", 100)
my_tesla.display_info()