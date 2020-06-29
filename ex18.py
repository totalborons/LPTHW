
def print_two(*args):
    first_one, second_one = args
    print(f"First one is {first_one} and second one is {second_one}")

# About multiple functions with the same name called method overloading .. it is absent in python so need to have a different name for each one of them...


def print_two_again(arg1, arg2):
    print(f"Printing sepearely {arg1}, {arg2}")


def print_none():
    print("I got nothign")


print_two("Shikhar", "Mathur")
print_two_again("Piyush", "Aggarwal")
print_none()

# just one for commenting
