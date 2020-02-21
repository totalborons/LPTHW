from sys import argv
script,fileName=argv
txt=open(fileName)

print(f"Opening file {fileName}")
print(txt.read())
#done now


#have to pass txt extension in name else it wont work
#read() reads all the lines in the file