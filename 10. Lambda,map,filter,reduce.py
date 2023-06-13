# LAMBDA
def double(x):
    return x * 2
print(double(3))

y = lambda x: x * 2  # pass on the variable before colon, it will return values after the colon
print(y(4))

z = lambda x, y: x + y if x > y else 0
print(z(2,3))

zz = lambda x, y: x * 90 if x > y else 0
print(zz(4,3))

zz = lambda x, y: "hello" if x > y else 0
print(zz(4,3))


# MAP
# apply same function to each item of input sequence
# List [m, n, p] fucntion f() ---> map box ---> New list , [f(m),f(n),f(p)]
n = [1,2,3,4]
# lambda x:x**2 function to be applied to each item in the list "n"
# map(fuction, list)  --> map(lambda x:x**2,n)
print(list(map(lambda x:x**2,n)))

# FILTER
# Filter items from the list and retuns the filtered list
# List [m,n,p], condition ---> Filter if m==condition ---> New list [m,n]
n = [1,2,3,4]
print(list(filter(lambda x:x if x>2 else 0, n)))
print(list(filter(lambda x:x>2, n)))


# REDUCE
# apply same operation to each item of input sequence, use result of operation as first param of next operation
# return an item and not the entire list
# List [m, n, p] fucntion f(x,y) ---> map box --->  f(m,n),p THEN  f(f(m,n),p)
# it will take the first 2 parameter from the list for x and y then apply the resutl and just join with rest of list
import functools
# List [m,n,p], condition ---> Filter if m==condition ---> New list [m,n]
n = [1,2,3,4]
print(functools.reduce(lambda x,y:x*y,n))


# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

##---

from setuptools import reduce #importing reduce module for using reduce function

l1 = [2,3,4,5,6]

mapping_the_l1 = list(map(lambda x: x*2, l1)) # MAP FUNCTION APPLIES THE GIVEN COMMAND TO EVERY INDEX OF A LIST
# IN THIS CASE WE ARE MULTIPLYING EVERY CHARACTER IF LIST l1 TO 2 USING LAMBDA FUNCTION

print(mapping_the_l1)


filtering_the_l1 = list(filter(lambda x: x%2 ==0, l1)) #FILTER FUNCTION FILTERS THE LIST ACCORDING TO OUR WISH
# IN THIS CASE WE ARE FILERING THE NUMBER WHICH IS DIVISIBLE BY 2 IN l1.

print(filtering_the_l1)

def add(x, y):
   return x+y
   
reducing_the_l1 = reduce(add, l1) # REDUCE FUNCTION IS USED FOR DOING MATHEMATICAL OPERATIONS IN A LIST
# HERE, WE ARE ADDING ALL THE CHARACTERS LIST l1 

print(reducing_the_l1)
