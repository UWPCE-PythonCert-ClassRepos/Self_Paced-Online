#!/usr/bin/env python3

import os
import pathlib

# Activity 2: File lab
print('\nFile Lab\n')

# prints full path name
for file in os.listdir():
    print(os.getcwd() + '/' + file)

# prints file names in current directory, regardless of operating system
[x for x in pathlib.Path('./').iterdir()]


# need to handle size of file, test with txt and binary files
with open('Path/to/fin', 'rb') as fin, open('Path/to/fout', 'wb') as fout:
    fout.write(fin.read())
