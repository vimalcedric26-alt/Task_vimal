class Vehicle:
    def __init__(self, model, rent_per_day):
        self.model = model
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return self.rent_per_day * days

    def vehicle_wheel(self):
        return "Vehicle wheel information"


class Truck(Vehicle):
    def vehicle_wheel(self):
        return "Truck has 8 wheels"


class Car(Vehicle):
    def vehicle_wheel(self):
        return "Car has 4 wheels"


class Bike(Vehicle):
    def vehicle_wheel(self):
        return "Bike has 2 wheels"


truck = Truck("Tata", 2000)
car = Car("Hyundai", 1500)
bike = Bike("Yamaha", 500)

days = 3

print("Truck Model:", truck.model)
print("Wheels:", truck.vehicle_wheel())
print("Rent for", days, "days:", truck.calculate_rent(days))

print("\nCar Model:", car.model)
print("Wheels:", car.vehicle_wheel())
print("Rent for", days, "days:", car.calculate_rent(days))

print("\nBike Model:", bike.model)
print("Wheels:", bike.vehicle_wheel())
print("Rent for", days, "days:", bike.calculate_rent(days))
