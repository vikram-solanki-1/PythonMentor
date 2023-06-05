# First-Class Functions
def square(x):
    return x * x

# f = square()  # this will give error as () means we want to execute the function, but we dont, we just reassigned it
f = square
g = square(5)

print(square)  # <function square at 0x100348540>
print(f)        # <function square at 0x100348540>
print(g)        # 25
print(f(5))      # 25 calling function by passing the argument value.
print(square(5))  # 25 but having them in () means function will get executed for passed values


## Passing function into a function
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
 
square_object = my_map(square, [1,2,3])
cube_object = my_map(cube,[1,2,3])
print(square_object)
print(cube_object)


## Half function execution and then wait for another half
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text
h1 = html_tag('h1')  # at this point it just equals to wrap_text function waiting for more inputs
h1('Test headline')  # now, wrap_text function got its input and returned output from function
h1('Another headline')
p = html_tag('p')
p('Paragraph 1')


### CLOSURE
# using argumnet
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
   #1 return inner_func() # executing the inner function so, it will return print(message) which is Hi
    return inner_func  # we are creating a function, but not executing it, so it will return function
#1 outer_func() # this would have returned print Hi from #1
my_func = outer_func()  # this is a function which is equal to inner_func
print(my_func.__name__)
my_func() # now we are executing inner function
my_func() # inner function executed twice, although outer function is executed only once
my_func() # inner function executed 3 times, although outer function is executed only once

# using parameter
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

# simplified
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

#  closure is INNER function that remembers and has access to variables in local scope in which it was created.
#  even after outer function finished executing.


##### DECORATOR
# simple decorator
def decorator_func(original_func):  # passing function as parameter
    def wrapper_func():
        print('Wrapper function executed before {}'.format(original_func.__name__))
        return original_func()  # executing parameter function and returning output

    return wrapper_func

def display():
    print('This is parameter function, it will be executed in wrapper function')

decorated_display_variable = decorator_func(display)
decorated_display_variable() # when wrapper function is executed, it in truns executes the display function.


# -------------  @ decorator --------------------------
def decorator_func(original_func):  # passing function as parameter
    def wrapper_func():
        print('Wrapper function executed before {}'.format(original_func.__name__))
        return original_func()  # executing parameter function and returning output
    return wrapper_func

@decorator_func  # function will be passed as input to decorator_func and then its fate lies there
def display():
    print('This is parameter function, it will be executed in wrapper function')

display() # it first goes inside decorator_func and then get executed there.
# if we remove the @decorated function then display function will execute and decorator_func will not execute


#------------- @ decorator with multiple arguments ---------------------
def decorator_func(original_func):  # passing function as parameter
    def wrapper_func(*args, **kwargs):
        print('Wrapper function executed before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)  # executing parameter function and returning output
    return wrapper_func

@decorator_func  # function will be passed as input to decorator_func and then its fate lies there
def display():
    print('This is parameter function, it will be executed in wrapper function')

display() # it first goes inside decorator_func and then get executed there.
# if we remove the @decorated function then display function will execute and decorator_func will not execute

print("--------gap between second decorator function-------")

# @decorator_func this will cause issue as wrapper_func takes 0 args, but we are passing 2 args here.
# so we need to modify wrapper_func to take more args
@decorator_func
def display_info(name,age):
    print('display info ran with arguments {} {}'.format(name,age))
display_info('vikram',38) # now this function first goes into decorator_func and then into wraper func and then executes



