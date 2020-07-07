# this is python now... on 7th Julyyy...
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there aren't 10 things in that list.Let's fix that")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song",
              "Franchise", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    # pop takes from the top of the stack or the nth element which is the end...
    print("Adding another one", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go", stuff)
print("Let's do something with stuff")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
# here the corn is left out as it was popped off???
print(len(stuff))
# once the stuff is popped off from a list.. it ceases to be a part of it

print('#'.join(stuff[3:7]))
# this includes the 3rd index but not the 7th index...
