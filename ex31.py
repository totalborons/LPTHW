# this is using the else if statement which is written here as elif....
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take cars")
elif cars < people:
    print("We should not take cars")
else:
    print("We can't decide")

if trucks > cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("We can take the trucks")
else:
    print("W still can't decide")

if people > trucks:
    print("Alright lets just take the trucks")
else:
    print("Alright lets just stay at home..")

    # the logics doesn't make sense here.. its just a simple exercise for it....
