class Employee:
    raise_amount = 1.1  # class global variable
    num_of_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emp += 1  # since INIT method runs each time we create emp object, the count will increase

    def fullname(self):  # if we leave it blank without (self) it will give error --> Employee.fullname() takes 0 positional arguments but 1 was given
        # when fullname get called later, (Self) will be passed by default as argument, so, (self) is required to handle it.
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return int(self.pay * self.raise_amount)  # OR return int(self.pay * Employee.raise_amount)
        # return int(self.pay * raise_amount) # this will give error

emp_1 = Employee('Vikram', 'Solanki', 100000)

print(emp_1)  # its gives the class type object # <__main__.Employee object at 0x104b21410>
print(emp_1.email)  # prints the attribute values # Vikram.Solanki@company.com
print(emp_1.fullname())  # since fullname is function we need () to get return captured. # Vikram Solanki
print(Employee.fullname(emp_1))  # Since we are directly calling class we need to pass values via instance emp_1

emp_2 = Employee('Vikram2', 'Solanki2', 100000)
emp_3 = Employee('Vikram3', 'Solanki3', 100000)

print(emp_2.apply_raise())  # function is called
print(Employee.num_of_emp)  # 3

print('-----Class inheretence ------')
class Engineer(Employee):
    active = True
    def EmpRole(self):
        print("This Employee is engineer")

print(Engineer.EmpRole('g'))  # to call function i need to pass 1 argument

Eng = Engineer('Eng','Emp',150000)  # to create child class object i need to pass input as per parent calss, so 3 inputs needed
print(Eng.apply_raise()) # we called parent class function
print(Eng.EmpRole()) # we called child calss function

print('-----multi level class ------')
class EngManager(Engineer):
    pass
    print('Engineering Manager')


EngManager = Engineer('Eng','Emp',150000)
print(EngManager.apply_raise())

# --------------------super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

# --------------------super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())


## abstract
#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class to make sure they dont miss creating this method

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")  #this method/fucntion is needed as its defined in abstact
    def stop(self):                  # so we are ensuring not missing any essential implementation
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()

