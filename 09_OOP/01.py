class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()

my_new_car = Car("Honda", "Civic")
my_new_car.display_info()