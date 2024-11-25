class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"Bike: {self.brand} {self.model}, Type: {self.bike_type}"

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return f"Truck: {self.brand} {self.model}, Capacity: {self.capacity} tons"

car = Car("Toyota", "Corolla", 4)
bike = Bike("Giant", "ATX", "Mountain")
truck = Truck("Volvo", "FH16", 20)

print(car.info())
print(bike.info())
print(truck.info())