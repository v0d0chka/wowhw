class Car:
    def __init__(self, year_of_manufacture, manufacturer, brand, fuel_consumption):
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.brand = brand
        self.probeg = 0
        self.fuel_consumption = fuel_consumption

    def drive(self):
        print(f"Я авто марки {self.brand}, їду")

    @property
    def cost_of_service(self):
        return self.probeg * 7.6


car1 = Car(year_of_manufacture=2020, manufacturer="Toyota", brand="Corolla", fuel_consumption=6.5)
car2 = Car(year_of_manufacture=2018, manufacturer="Ford", brand="Focus", fuel_consumption=7.2)

car1.probeg = 15000

print(f"Вартість обслуговування {car1.brand}: {car1.cost_of_service}")

car2.drive()