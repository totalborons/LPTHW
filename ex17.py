from sys import argv
from os.path import exists

script, from_path, to_path=argv
target_from=open(from_path,'r')


print(f"Writing files from {from_path} to {to_path}")

print(f"Does file exists of final file? {exists(to_path)}")
print(f"Does initial file present? {exists(from_path)}")
print("To prevent enter CTRL-C")
input('?')
target_to=open(to_path,'w')
print("Transfering file.......")
content=target_from.read()
target_to.write(content)
print("File transferred")
target_from.close()
target_to.close()

