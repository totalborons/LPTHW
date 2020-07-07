# dictionaries here..
# basic way is list of storing data which is like array we talked about earlier

# another data format is Dictionary which seems to be very imp.. we can select an element not only on the basis of index but also on the basis of content/like in actual disctionaries
# dict seems like a JSON file here in python

states = {
    "Oregon": "OR",
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    "Michigan": 'MI'
}
cities = {
    'CA': "San Francisco",
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print('-'*10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])
print('-'*10)
print("Michigan's abbreviation is--", states['Michigan'])
print("Florida's abbreviation is--", states['Florida'])
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has city {city}")


print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    print(f"and has city{cities[abbrev]}")
# one thing absent here it doesn't check if its actually present in the second list or will throw an error here...

print('-'*10)
state = states.get('Texas')

if not state:
    print("Sorry no texas")

city = cities.get('TX', 'Does not exist')
# the second is the default value to return like -9999 we used to do in android programming for errors there...

print(f"The city for the state 'TX' is {city}")
# a thing to remember is dictionaries do not have order like list...
# it is for key value pairs only here...
