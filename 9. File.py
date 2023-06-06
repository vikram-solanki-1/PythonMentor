# ------------Read-File--------------
with open('copy.txt') as file_1:   # with open will close file automatically after function is done.
    print(file_1.read())
#----
content = open('copy.txt','r')
print(content.read())
content.close()
    
## using file name as variable
filename = 'copy.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
print(contents)
#-- from location
f_path = "/Users/applemacbookair/Desktop/PyCharm123/copy.txt"
with open(f_path) as f_obj:
    content = f_obj.read()
print(content.rstrip())

# ------------Write-File--------------
filename = 'copy.txt'
with open(filename, 'w') as f_obj:     # with open(filename, 'a') as f_obj: for appending the file
    f_obj.write("I am liking programming\n")
    f_obj.write("I 2 liking programming\n")
    f_obj.write("I 3 liking programming")
with open(filename) as f_r:
    content = f_r.read()
print(content)

#---anither write
text = "hi i am writing on this file\nThis is some text\nHave a good one!\n"
with open('copy.txt','w') as file:
    file.write(text)

# ------------check-File--------------
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
    
 
 # exception handling
 try:
    with open('test.txt') as file:  # be default open is with 'r' for read, we can pass argument 'w' for write 'a' for append
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
 # -----------------


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

   
   
   
    
