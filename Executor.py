class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color): # attributes are passed as argument.
        self.make = make  # we can assign self.make value received from argument make
        self.model = model    # instance variable
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")


car_1 = Car("Chevy", "Corvette", 2021, "blue")  # car1 object created with arguments passed to it.
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.drive()
