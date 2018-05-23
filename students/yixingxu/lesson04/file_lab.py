#!/usr/bin/env python3
# Activity 2: File Lab
# Write a program which prints the full path for all files in the current directory, one per line
import os
import pathlib

cwd = os.getcwd()
path = pathlib.Path(cwd)
for full_path in path.iterdir():
    print(full_path)
    
# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command). 
def copy_file(source,dest):
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())
    
if __name__ == "__main__":
    source = input('Enter source file name: ')
    dest = input('Enter destination file name: ') 
    source = 'test_source.txt'
    dest = 'test_dest.txt'
    copy_file(source,dest)
    source = 'test_source.JPG'
    dest = 'test_dest.JPG'
    copy_file(source,dest)    