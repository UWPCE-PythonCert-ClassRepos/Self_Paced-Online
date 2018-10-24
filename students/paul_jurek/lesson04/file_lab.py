# Activity 2: File Lab
# Goal:
# Get a little bit of practice with handling files and parsing simple text.
# Paths and File Processing
# Write a program which prints the full path for all files in the current directory, one per line
# 
import pathlib

pth = pathlib.Path('./')
for f in pth.iterdir():
    print(f)

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command). 
# we will copy lesson 3 file to lesson 4 for this
# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
def copy_file(old_file, new_file):
    """does content copy of files from old file to new"""
    
    with open(old_file, 'rb') as infile, open(new_file, 'wb') as outfile:
        while True:
            line = infile.readline()
            if not line:
                break
            outfile.write(line)

# testing this script
original_file = '../lesson03/slicing_lab.py'
new_file = 'slicing_lab_copy2.py'
copy_file(old_file=original_file, new_file=new_file)

# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
# Test it with both text and binary files (maybe jpeg or something of your chosing).