# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:02:03 2018

@author: dennis
"""
import os

#Paths and File Processing
#Write a program which prints the full path for all files in the current directory, one per line
print(f'\nCurrent working directory:')
print(os.getcwd())

#Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command). 
source = 'dict_lab.py' #source file name
dest = 'temp.py' #destination file name
with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
    outfile.write(infile.read())
    
#Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
#This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') 
#(or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
#Test it with both text and binary files (maybe jpeg or something of your chosing).
def copy_file(input_file, output_file):
    outfile = open(output_file, 'wb')
    inputfile = open(input_file, 'rb')
    while True:
        line = inputfile.readline()
        if not line:
            break
        outfile.write(line)
    outfile.close()

# Testing copy_file function for different types of files.
copy_file('mailroom.py', 'output.txt') # text file
copy_file('tulips.jpg', 'flower.jpg') # picture file