# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:24:01 2018

@author: Laura.Fiorentino
"""
import pathlib
path = pathlib.Path()
absolute_path = path.absolute()
print('Print the full path for all files')
for files in path.iterdir():
    print(absolute_path / files)
print()
print('Copy a file from a source to a destination')
file = open('testtext.txt', 'rb')
file_contents = file.read()
file2 = open('newtesttext.txt', 'w+b')
file2.write(file_contents)
print('Copied tsttxt.txt to newtesttex.txt')
file3 = open('noaalogo.jpg', 'rb')
file3_contents = file3.read()
file4 = open('noaalogonew.jpg', 'w+b')
file4.write(file3_contents)
print('Copied noaalogo.jpg to noaalogonew.jpg')
