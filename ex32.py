the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]
for number in the_count:
    print(f"The count variable value is {number}")

for fruit in fruits:
    print(f"The name of the fruit is {fruit}")

for i in change:
    print(f"The mixed variable value is {i}")

# adding and making new list dynamically
elements = []
# empty declaration of a list

for i in range(0, 6):
    print(f"Adding this to the list{i}")
    # this is upto 5 times only.. so this range is  <6 and not <=6
    elements.append(i)

for i in elements:
    print(f"Value in elements is{i}")
