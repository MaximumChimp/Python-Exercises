#PROBLEM: Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.
#PURPOSE:  This exercise introduces Object-Oriented Programming (OOP). Instead of just writing functions, you are creating a “Blueprint” (the Class) to generate “Objects” (the specific cars). This is how modern software is built, allowing you to organize code into logical, reusable components.

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")

new_car =  Car("Toyota","Camry",2022)

new_car.start_engine()
print(new_car.make)
print(new_car.model)
print(new_car.year)