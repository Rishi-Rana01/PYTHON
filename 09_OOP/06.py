#Total car

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    def display_info(self):
        print(f"Car Brand: {self.__brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Full Name: {self.full_name()}")
        print(f"Fuel Type: {self.fuel_type()}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electricity"

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Fuel Type: {self.fuel_type()}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()



my_tesla = ElectricCar("Tesla", "Model S", 100)
my_tesla.display_info()