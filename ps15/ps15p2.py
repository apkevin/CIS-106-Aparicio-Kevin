'''
2.	Create a car class. This should have methods for make, model, sticker price and discount price 
(90% of sticker price). Then create a derived class called sport. Inherit the car class but add options methods. 
Set the option to Y to include the option in the updated price method. See table below. Define a method for each option.

Option (method)	Option Price

SportWheels		1000.00
SportEngine		3000.00
SportInterior   2000.00

For each method set to Y add the amounts to the updated price and display using a method called pricewithoptions. 

Write program to instantiate the object and show that it works. 

'''

class Car:
    def __init__(self, make, model, price, sportCar):
        self.make = make
        self.model = model
        self.price = price
        self.sportCar = sportCar
    
    def discounted(self):
        b = float(self.price) - float(self.price) * .90
        return b

class Sport(Car):
    def wheels(self):
        pass

    def engine(self):
        pass

    def interior(self):
        pass


car1 = Car("Honda", "Civic", 21000)
car2 = Car("Porsche", "911", 80000)

print(car1.make)
print(car1.model)
print(car1.price)
print(car1.discounted())
print(car2.discounted())