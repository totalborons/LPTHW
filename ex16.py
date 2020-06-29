from sys import argv

script, fileName = argv
print(f"Im going to delete the file {fileName}")
print("if you do not want to delete it press CTRL-C\n Else just hit enter")
input('?')

print("Truncating file now")
target = open(fileName, 'w')
# open command also have permissions attached to it.. unique to see it run on a linux machines and interact with the permission of the system thereß


print("truncating file now....")
target.truncate()

# this doesnt delete the file but empties the file.. arguments???

print("Now enter three lines to write")
line1 = input()
line2 = input()
line3 = input()
target.write(line1+'\n'+line2+'\n'+line3+'\n')
# here have to change the lines individually as write writes it in a sequential order without changing lines

print("Now ending the program")
target.close()

# always remember to close the files here else you will always have some error if reading it again at same runtime here...


# the '+' function lets you add the text but ','  doesnt like it would in print....
