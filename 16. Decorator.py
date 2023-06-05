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

