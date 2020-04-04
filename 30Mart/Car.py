class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descripitive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


myNewCar = Car('audi', 'a4', 2016)
print(myNewCar.get_descripitive_name())
myNewCar.odometer_reading = 23

secondCar = Car('ford', 'focus', 2017)
print(secondCar.get_descripitive_name())
secondCar.odometer_reading = 23
