import os
path = "/Users/applemacbookair/Desktop/PyCharm123/test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

# read file data
with open('/Users/applemacbookair/Desktop/PyCharm123/test.txt') as file_1:   # with open will close file automatically after function is done. 
    print(file_1.read())
 
 # exception handling
 try:
    with open('test.txt') as file:  # be default open is with 'r' for read, we can pass argument 'w' for write 'a' for append
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
    
  with open('/Users/applemacbookair/Desktop/PyCharm123/test.txt') as file_1:
    print(file_1.read())

text = "hi i am writing on this file\nThis is some text\nHave a good one!\n"
with open('test.txt','w') as file:
    file.write(text)
    
text = "\nappend the file\nThis is some text!\n"
with open('test.txt', 'a') as file_2:
    file_2.write(text)
with open('/Users/applemacbookair/Desktop/PyCharm123/test.txt') as file_2:
    print(file_2.read())


# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst

# Python move replace file
import os
source = "C:\\Users\\User\\Desktop\\source.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
    
    
# delete file or directory
import os
import shutil

path = "test.txt"

try:
    os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    #shutil.rmtree(path)#delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

    -----------
    # Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
   
   
    
