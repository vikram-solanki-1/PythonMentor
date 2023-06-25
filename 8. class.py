# class holds attributes and methods(actions)
# Methods are functions defined inside body of a class. methods define behavior of objects.  
# Example - Emp is a class, its attributes are Name & Age and its Methods are Perform job and Give presentation
# Example - Car is a class, its objects are Ford, GM , Tesla
# Inheritance is creating a new class that uses all properties, its called derived class. Human is interence class, Persona is derived class

class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color): # attributes are passed as argument
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


# -----if car module is defined---------
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()

print(car_1.wheels)
print(Car.wheels)

car_2.wheels = 2   # we can update variable for 1 object. or entire class by car.wheel = 2
print(car_2.wheels)  # this becomes car_2 variable which is already reassinged as 2
print(Car.wheels)   # this is still class level variable

# Inheretence-------------------
class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

Hawk.fly()  # this will throw error because it needs exactly 1 argument.
Hawk.fly('hi') # this will execute Hawk method

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
Hawk.fly()


# ------multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class

# -----------------------------------------------------------------------------
# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()

# -------------method override
class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()

# -------------method chaining
# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# car.turn_on().drive()
# car.brake().turn_off()
#car.turn_on().drive().brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
    
    
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


# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

  # Constructor
  def __init__(self, name, email, age):
      self.name = name
      self.email = email
      self.age = age

      # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
      self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
      self.age += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
      User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())

#Encapsulation -->
brad.print_encap()
brad._private = 800 #Changing for brad
brad.print_encap()

# Method inherited from parent
janet.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet._private = 600
janet.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad.print_encap()

####################################################################################
######### class detailed example ###################
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # if we leave it blank without (self) it will give error --> Employee.fullname() takes 0 positional arguments but 1 was given
        # when fullname get called later, (Self) will be passed by default as argument, so, (self) is required to handle it.
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Vikram', 'Solanki', 100000)

print(emp_1)  # its gives the class type object
print(emp_1.email)  # prints the attribute values
print(emp_1.fullname())  # since fullname is function we need () to get return captured.
print(Employee.fullname(emp_1))  # we can directly call parent class but we need to pass values via instance emp_1
print(emp_1.fullname())  # since fullname is function we need () to get return captured.
### result
# <__main__.Employee object at 0x101480a50>
# Vikram.Solanki@company.com
# Vikram Solanki
# Vikram Solanki


class Employee:
    raise_amount = 1.1
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
        return int(self.pay * self.raise_amount)
        # using self.pay will allow to use specific raise amount for that instance ELSE it will take CLASS variable value
        # self.pay = int(self.pay*1.1)  # if we want to print attribute
       # return int(self.pay*raise_amount) # this will give error as we need to call class variable using CLASS or CLASS instance

emp_1 = Employee('Vikram', 'Solanki', 100000)
emp_2 = Employee('Vikram2', 'Solanki2', 200000)

print(emp_1.pay)  # prints the attribute values
print(emp_1.apply_raise()) # function is called
print(emp_1.raise_amount)
print(Employee.num_of_emp)

# 100000
# 110000
# 1.1
# 2


######## REGULAR METHOD, CLASS METHOD & STATIC METHODS ####################
# Regular - automatically takes self as the first argument, which means it takes instance/class as first argument 

















