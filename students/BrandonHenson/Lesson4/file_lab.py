#import os
#for i in os.listdir(os.getcwd()):
#    print(os.path.abspath(i))



sourcefile = input('Enter the path for a file you want to copy')
fileobj = open(sourcefile)
objfilenew = sourcefile + "new.txt"
destinationfile = open(objfilenew, "w")
for line in fileobj:
    fileobj.readline(0)
    destinationfile.write(line)

