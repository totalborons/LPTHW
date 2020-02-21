from sys import argv
script ,fileNaam=argv
def rewind(fileName):
    fileName.seek(0)

def readWhole(fileName):
    print(fileName.read())

def readLine(lineNumber,fileName):
    print(lineNumber,fileName.readline(),end='')

file=open(fileNaam,'r')
print("reading whole file")
readWhole(file)
print("rewinding")
rewind(file)
readLine(1,file)
readLine(2,file)
readLine(3,file)

file.close()