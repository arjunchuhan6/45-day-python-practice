#create a car class with attributes make, model, and year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
print("Car class created successfully.")
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)
car4 = Car("Chevrolet", "Malibu", 2018)
print(f"Car 1: {car1.make} {car1.model}, Year: {car1.year}")
print(f"Car 2: {car2.make} {car2.model}, Year: {car2.year}")
print(f"Car 3: {car3.make} {car3.model}, Year: {car3.year}")
print(f"Car 4: {car4.make} {car4.model}, Year: {car4.year}")