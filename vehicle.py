# Define a class called "Vehicle"
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")

# Create a subclass "Car" that inherits from "Vehicle"
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk_horn(self):
        print(f"The {self.make} {self.model}'s horn honks: Honk! Honk!")

# Create a subclass "Motorcycle" that inherits from "Vehicle"
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        if self.has_sidecar:
            print(f"The {self.make} {self.model} cannot perform a wheelie with a sidecar.")
        else:
            print(f"The {self.make} {self.model} pops a wheelie!")

# Create instances of the "Car" and "Motorcycle" classes
my_car = Car("Toyota", "Camry", 2022, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, False)

# Call methods on the objects
my_car.start_engine()
my_car.honk_horn()

my_motorcycle.start_engine()
my_motorcycle.wheelie()
