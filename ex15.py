from sys import argv
script, fileName = argv
txt = open(fileName)

print(f"Opening file {fileName}")
print(txt.read())


# .read reads the whole file here and not the individual lines and no control over where and how to read..

# done now


# have to pass txt extension in name else it wont work
# read() reads all the lines in the file
