# A summary of all the things I've learned.., in this and the next file
print("Lets practice this")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs.")
poem = """
\t The lovely world with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

# all things above is about how to write hard coded strings with all the sequences


print("-"*10)
print(poem)
print('-'*10)
five = 10-2+3-6
print(f"This should be {five}")


# can return multiple variables from a function here unlike java

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates


start_point = 10000

# take multiple return elements in different variables
beans, jars, crates = secret_formula(start_point)

print("With the starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars and {crates} crates")

start_point = start_point/10

print("We can also do it this way")

# take multiple variables return into a single array??? like args???
formula = secret_formula(start_point)


print("We'd have {} beans, {} jars and {} crates".format(*formula))
