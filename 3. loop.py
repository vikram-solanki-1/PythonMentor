my_list1 = [1, 2, 3, 4, 5, 6]  # it's a list
#  add 5 to each element in the list
for element in my_list1:
    element = element + 5
    print(element)
# indent is needed so that it takes code as part of for loop.
# Enters the loop with colon and exits the loop after indent is not present.

#  IF loop - Else should not be indented and should have colon
a = 15
if a % 2 == 0:
    print("a is divisible by 2")
else:
    print("not divisible by 2")
    
# while loop example
i = 1
while i < 5: # while breaks when it comes back to run while condition
 print(i)
 i += 1

number = 1
while number < 6:
    print(number)
    if number == 4:
        break    # while is forcefully breaked at certain condition in the while loop
    number = number + 1
print("after while loop ended")
    
# while loop with else example
number = 1
while number <4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4")


#  While loop
from random import randint

moves = ["rock", "paper", "scissor"]
while True:
    computer = moves[randint(0, 2)]
    player = input("rock, paper or scissor? (or end the game)").lower()
    if player == "end the game":
        print("The game has ended")
        break  # Breaks the while loop
    elif player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You loose", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You loose", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    elif player == "scissor":
        if computer == "rock":
            print("You loose", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    else:
        print("check your spelling")  # after the else the program return to while and since while has no END condition it will keep getting executed


# For loop
 for item in 'Python':  # each iteration it will pick one itme at a time
    print(item)

for item in ['Nam1', 'Nam2', 'Nam3']:
    print(item)

for item in range(5, 10, 2):  # start from 5, skips 2 and print upto less than 10
    print(item)
    
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

        
  #   -----------
    # A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')

# Break
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range
for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1
