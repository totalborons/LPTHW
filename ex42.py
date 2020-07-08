# none here as basic class
class Animal(object):
    pass


# is-A
class Dog(Animal):
    # has-A
    def __init__(self, name):
        self.name = name

# is-A


class Cat(Animal):
    # has-A
    def __init__(self, name):
        self.name = name

# nothing here as basic class


class Person(object):
    # has-A
    def __init__(self, name):
        self.name = name
        self.pet = None
        # None is a new one.. i thought usually we use null

# is-A


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # different way of calling super here like in java...
        self.salary = salary

# none as simple class


class Fish(object):
    pass

# is-A


class Salmon(Fish):
    pass

# is-A


class Halibut(Fish):
    pass


rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Person")
mary.pet = satan
frank = Employee("frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
