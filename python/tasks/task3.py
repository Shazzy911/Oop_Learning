# Problem 3: Multilevel Inheritance (Medium)
# Task:

# Create a Vehicle class with a method start_engine() that prints "Engine started."
# Create a subclass Car that inherits from Vehicle and adds a method drive() that prints "Car is driving."
# Further subclass ElectricCar from Car, adding a method charge_battery().
# Steps:

# Create the base class Vehicle with the method start_engine().
# Inherit Vehicle to create the Car class and add drive() method.
# Further inherit Car to create ElectricCar, adding charge_battery().


class Vehicle:
    def __init__(self):
        pass

    def start_engine(self):
        print(f"Engine Started")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def drive(self):
        print(f"Car is driving")

class Electric_Car(Car):
    def __init__(self):
        super().__init__()

    def charge_battery(self):
        print(f"Charging battery of the Car")



car1 = Electric_Car()

car1.charge_battery()
car1.drive()
car1.start_engine()
