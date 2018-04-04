#!/usr/bin/env python3

import os

# prints full path for all files in current directory
for l in os.listdir():
    print("{}\{}".format(os.getcwd(),l))


#copeies a file from source to destination
print("your working directory is {}\n".format(os.getcwd()))
print("It contains the following files:")

for f in os.listdir():
    print(f)

source = input("\ntype the name of a file in your WD to copy -> ")

# assigns the file extension to 'ext' variable
ext = os.path.splitext(source)[1]

# opens 'source' with read binary arguement
# opens 'copied_file' with write binary arguement
# reads the input file (in_f) and writes it (out_f)
with open(str(source), 'rb') as in_f, open("copied_file" + ext, 'wb') as out_f:
    out_f.write(in_f.read())
