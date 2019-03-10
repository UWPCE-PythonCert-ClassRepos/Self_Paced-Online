'''
Name: Muhammad Khan
Date: 03/05/2019
Assignment04

'''
import os


# Activity 2: File Lab.
# prints the full path for all files in the current directory, one per line
for file in os.listdir():
    print(os.path.abspath(file))

# Write a program which copies a file from a source, to a destination
# (without using shutil, or the OS copy command).

def read_write_file(input, output):
    with open(input,'rb') as input_file, open(output,'wb+') as output_file:
        output_file.write(input_file.read())
    input_file.close();output_file.close()

read_write_file('input_file.txt','output_file.txt')
read_write_file('Orange.jpg','OrangeOutput.jpg')
read_write_file('Orange.jpg','OrangeOutput.txt')





