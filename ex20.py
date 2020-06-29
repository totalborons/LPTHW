from sys import argv
script, fileNaam = argv


def rewind(fileName):
    fileName.seek(0)

# this is 0th index starting with the file for each character,... is new file a new character?????
# end of line character seems to be an escape sequence character as with the 13th index first line comes as blank....
# hence seek is character index which includes the escape sequences somehow...


def readWhole(fileName):
    print(fileName.read())


def readLine(lineNumber, fileName):
    print(lineNumber, fileName.readline(), end='')


file = open(fileNaam, 'r')
print("reading whole file")
readWhole(file)
print("rewinding")
rewind(file)
readLine(1, file)
readLine(2, file)
readLine(3, file)

file.close()

# little unclear about how the seek function works with the readwhole thing.. and also with the readline thing..
