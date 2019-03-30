#!/usr/bin/env python3

# Write a program which prints the full path for all files in the current directory, one per line

import pathlib
import sys

file = pathlib.Path('./')
for f in file.iterdir():
    print(f)


# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
def copy_file(sourceFileName, destFileName):
    # Take second and third elements from the arguments array (first one is 'program.py' itself)
    #sourceFileName = sys.argv[1]
   #destFileName = sys.argv[2]

    # Open file 'sourceFileName' for reading as binary
    sourceFile = open(sourceFileName, "rb") 
    data = sourceFile.read()
    sourceFile.close()

    # Open (or create if does not exists) file 'destFileName' for writing as binary
    destFile = open(destFileName, "wb") 
    destFile.write(data)
    destFile.close()

