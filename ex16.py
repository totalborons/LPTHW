from sys import argv

script, fileName= argv
print(f"Im going to delete the file {fileName}")
print("if you do not want to delete it press CTRL-C\n Else just hit enter")
input('?')

print("Truncating file now")
target=open(fileName,'w')
print("truncating file now....")
target.truncate()
print("Now enter three lines to write")
line1=input()
line2=input()
line3=input()
target.write(line1+'\n'+line2+'\n'+line3+'\n')
print("Now ending the program")
target.close()


### the + function lets you add the text but the comma thign doestn atleast in write parameter
