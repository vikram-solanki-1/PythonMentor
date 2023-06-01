# Single quotes in middle of string
course = "Python's course by Vikram" #  text with single quote
print(course)
print(course[-1])
print(course[3])
# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]
print(course[0:3])  # starts from 0 till 3 but excludes 3rd character
print(course[2:])  # 0 to end
print(course[:3])  #  be default it takes 0 for start position
print(course[:])   # close original text, it starts with 0 end in total length
course = 'Python"s course by Vikram' # text with double quote
print(course)
course = '''                         # text with long message           
Hi Vikram
Here is the long text in python
Thank you
'''
print(course)


# formatted string
first = 'Vikram'
last = 'Solanki'
message = first + ' [' + last + '] is teaching us python'
msg = f'{first} [{last}] is teaching us python'
print(message)
print(msg)

course = 'Python course by Vikram'
print(len(course))  # general purpose function for counting
print(course.upper())  # upper is a string method, len & print are function as they belong to string or number or
# other kind of objects. this is the difference between function and method.
# so it will not modify the value of course in program, just locally the next print will give original value
print(course)
print(course.find('cou'))
var1 = course.replace('course', 'tutorial')
print(var1)
print(course)
print('Python' in course)
print('python' in course)
#  find return index and in returns the boolean value

# Arithmetic Operations 

# Data types int, float, string, boolean
birth_year = input('Birthyear ? ')
age = 2023 - int(birth_year)
print(type(age))
print(age)


/ # returns a float
// # returns an int
% # returns the remainder of division
** # exponentiation - x ** y = x to the power of y

#True/Fasle operator
High_income = False
Good_Credit = True
missed_payments = True
if High_income or Good_Credit and not missed_payments:
    print("Eligible for loan")
    
 






