#this is about variables
cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passengers_per_car=passengers/cars_driven
print("There are",cars,"available")
print("There are",cars_driven,"cars which are being used")
print("Car pool capacity is",carpool_capacity,"people")
print("Average numebr of people in each driven car is",average_passengers_per_car,"people")