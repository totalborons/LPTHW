from sys import argv

# another import here to see if file exists or not....
from os.path import exists

script, from_path, to_path = argv
target_from = open(from_path, 'r')
# permission to read.


print(f"Writing files from {from_path} to {to_path}")

print(f"Does file exists of final file? {exists(to_path)}")
print(f"Does initial file present? {exists(from_path)}")
print("To prevent enter CTRL-C")
input('?')
target_to = open(to_path, 'w')
# still the same command for writing as it is for reading... open and close simple...

print("Transfering file.......")
content = target_from.read()
# reads the whole file at once like always...
target_to.write(content)
# simplest write command here....

print("File transferred")
target_from.close()
target_to.close()
# close both reading and writing files..
