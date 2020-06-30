i = 0
elements = []

while i < 6:
    print(f"The value of i is {i} at the start")
    elements.append(i)
    i += 1
    print(f"The value of i is {i} at the end")

print("Loop ended")

for i in elements:
    print(f"The values are {i}")
