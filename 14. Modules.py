import math # to access math function available in this module
# or import math as m -- this will import math module
# from math import pi -- this will import pi function from math module
# its prefered to import module over function as when we use module.function then we avoid error chance 
# as it is possible we have variable with same name as function name defined in math module
print(math.ceil(2.8))
# or print(m.ceil(2.8))

print(help("modules"))
print(help("math"))

# create a ConverterModule.py with classes OR Functions in it such  as lb_to_kg and kg_to_lb
# we can resume the function and class code from this file into other code by following command
# ConverterModule.py
def lb_to_kg(weight):
    return weight * .45

def kg_to_lb(weight):
    return weight / .45
# import 1
import ConverterModule
print(animals.kg_to_lb(20))

# import 2
from ConverterModule import kg_to_lb
print(kg_to_lb(20))
